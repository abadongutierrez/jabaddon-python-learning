import os
import hashlib
import pickle
from datetime import datetime, timedelta
from pathlib import Path
from typing import List
from docling.document_converter import DocumentConverter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from ..config.settings import settings
from ..config import constants
import logging

logger = logging.getLogger(__name__)

class DocumentProcessor:
    """
    Handles document parsing, caching, and chunking for efficient RAG processing.

    The DocumentProcessor class ensures efficient processing by:
    - Validating file sizes before processing
    - Using caching to avoid redundant processing of previously uploaded files
    - Extracting structured content from documents using Docling
    - Splitting text into chunks using MarkdownHeaderTextSplitter for better retrieval in vector databases

    This approach enables DocChat to efficiently retrieve relevant document chunks,
    making AI-powered retrieval-augmented generation (RAG) more scalable by leveraging:
    - Docling for structured content extraction
    - ChromaDB-compatible chunking for vector search
    - A caching system to avoid redundant processing
    """

    def __init__(self):
        """
        Initializes the document processor with cache settings and header structure.

        Sets up:
        - A predefined header structure for Markdown-based chunking (H1 and H2 headers)
        - A cache directory for storing processed document chunks
        - Ensures that the cache directory exists by creating it if necessary
        """
        # Define headers for Markdown text splitting (H1 and H2)
        self.headers = [("#", "Header 1"), ("##", "Header 2")]

        # Set up cache directory path from settings
        self.cache_dir = Path(settings.CACHE_DIR)

        # Create cache directory if it doesn't exist
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
    def validate_files(self, files: List) -> None:
        """
        Ensures that the total size of uploaded files does not exceed a predefined limit.

        Args:
            files (List): List of file objects to validate

        Raises:
            ValueError: If the total size exceeds constants.MAX_TOTAL_SIZE

        How it works:
        1. Computes the total size of all uploaded files
        2. Compares the total size against constants.MAX_TOTAL_SIZE
        3. Raises a ValueError if the limit is exceeded
        """
        # Calculate total size of all files
        total_size = sum(os.path.getsize(f.name) for f in files)

        # Check if total size exceeds the configured maximum
        if total_size > constants.MAX_TOTAL_SIZE:
            raise ValueError(f"Total size exceeds {constants.MAX_TOTAL_SIZE//1024//1024}MB limit")

    def process(self, files: List) -> List:
        """
        Handles the entire document processing pipeline, including caching and deduplication.

        Args:
            files (List): List of file objects to process

        Returns:
            List: List of unique document chunks ready for vector database insertion

        How it works:
        1. Validates the uploaded files using validate_files()
        2. Generates a hash of each file's content to check if it has been processed before
        3. If cached, loads the data from cache using _load_from_cache()
        4. If not cached, processes the file using _process_file() and stores results in cache
        5. Ensures that no duplicate chunks are stored across multiple files

        This approach prevents redundant processing and ensures efficient retrieval.
        """
        # Validate file sizes before processing
        self.validate_files(files)

        all_chunks = []
        seen_hashes = set()  # Track chunk hashes to prevent duplicates

        for file in files:
            try:
                # Generate content-based hash for caching
                with open(file.name, "rb") as f:
                    file_hash = self._generate_hash(f.read())

                # Determine cache file path based on content hash
                cache_path = self.cache_dir / f"{file_hash}.pkl"

                # Check if cached version exists and is still valid
                if self._is_cache_valid(cache_path):
                    logger.info(f"Loading from cache: {file.name}")
                    chunks = self._load_from_cache(cache_path)
                else:
                    # Process file and save to cache
                    logger.info(f"Processing and caching: {file.name}")
                    chunks = self._process_file(file)
                    self._save_to_cache(chunks, cache_path)

                # Deduplicate chunks across files to avoid storing identical content
                for chunk in chunks:
                    chunk_hash = self._generate_hash(chunk.page_content.encode())
                    if chunk_hash not in seen_hashes:
                        all_chunks.append(chunk)
                        seen_hashes.add(chunk_hash)

            except Exception as e:
                logger.error(f"Failed to process {file.name}: {str(e)}")
                continue

        logger.info(f"Total unique chunks: {len(all_chunks)}")
        return all_chunks

    def _process_file(self, file) -> List:
        """
        Converts the document into Markdown and splits it into structured text chunks.

        Args:
            file: File object to process

        Returns:
            List: List of document chunks split by Markdown headers

        How it works:
        1. Skips unsupported file types (only processes .pdf, .docx, .txt, and .md)
        2. Uses Docling's DocumentConverter to convert the file to Markdown
        3. Splits the extracted Markdown text using MarkdownHeaderTextSplitter

        This creates ChromaDB-compatible chunks optimized for vector search.
        """
        # Validate file type - only process supported formats
        if not file.name.endswith(('.pdf', '.docx', '.txt', '.md')):
            logger.warning(f"Skipping unsupported file type: {file.name}")
            return []

        # Convert document to Markdown using Docling
        converter = DocumentConverter()
        markdown = converter.convert(file.name).document.export_to_markdown()

        # Split Markdown text into chunks based on header structure
        splitter = MarkdownHeaderTextSplitter(self.headers)
        return splitter.split_text(markdown)

    def _generate_hash(self, content: bytes) -> str:
        """
        Generates a unique SHA-256 hash from document content.

        Args:
            content (bytes): The binary content to hash

        Returns:
            str: A hexadecimal SHA-256 hash string

        Use case: Helps in detecting duplicate files and chunks, enabling
        efficient caching and deduplication across the document processing pipeline.
        """
        return hashlib.sha256(content).hexdigest()

    def _save_to_cache(self, chunks: List, cache_path: Path):
        """
        Saves the processed document chunks in a pickle file for future use.

        Args:
            chunks (List): List of document chunks to cache
            cache_path (Path): File path where the cache should be saved

        How it works:
        Stores the chunks along with a timestamp for expiration checking.
        The timestamp allows the system to invalidate old cached data based
        on the CACHE_EXPIRE_DAYS setting.
        """
        with open(cache_path, "wb") as f:
            pickle.dump({
                "timestamp": datetime.now().timestamp(),  # For expiration checking
                "chunks": chunks
            }, f)

    def _load_from_cache(self, cache_path: Path) -> List:
        """
        Loads cached document chunks from a previously processed file.

        Args:
            cache_path (Path): File path to the cached data

        Returns:
            List: List of previously processed document chunks

        How it works:
        Opens the cached pickle file and extracts stored document chunks,
        enabling fast retrieval without reprocessing the document.
        """
        with open(cache_path, "rb") as f:
            data = pickle.load(f)
        return data["chunks"]

    def _is_cache_valid(self, cache_path: Path) -> bool:
        """
        Checks if the cached file is still valid (not expired).

        Args:
            cache_path (Path): Path to the cached file to validate

        Returns:
            bool: True if the cache exists and is not expired, False otherwise

        How it works:
        1. Checks if the cache file exists
        2. Compares the modification timestamp of the cached file against CACHE_EXPIRE_DAYS setting
        3. If the file is older than the expiration threshold, it is considered invalid

        This ensures that stale cached data is automatically refreshed.
        """
        # Check if cache file exists
        if not cache_path.exists():
            return False

        # Calculate age of cached file
        cache_age = datetime.now() - datetime.fromtimestamp(cache_path.stat().st_mtime)

        # Return True if cache is within expiration period
        return cache_age < timedelta(days=settings.CACHE_EXPIRE_DAYS)