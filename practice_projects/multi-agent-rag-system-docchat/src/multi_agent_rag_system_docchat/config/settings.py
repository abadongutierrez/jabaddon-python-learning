"""Settings and configuration management."""
import os
from pathlib import Path
from typing import Optional


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self):
        # OpenAI Configuration (for RelevanceChecker)
        self.OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
        self.OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        self.OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0"))
        self.OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "10"))

        # Research Agent Configuration
        self.RESEARCH_MODEL: str = os.getenv("RESEARCH_MODEL", "gpt-4o-mini")
        self.RESEARCH_TEMPERATURE: float = float(os.getenv("RESEARCH_TEMPERATURE", "0.3"))
        self.RESEARCH_MAX_TOKENS: int = int(os.getenv("RESEARCH_MAX_TOKENS", "300"))

        # Verification Agent Configuration
        self.VERIFICATION_MODEL: str = os.getenv("VERIFICATION_MODEL", "gpt-4o-mini")
        self.VERIFICATION_TEMPERATURE: float = float(os.getenv("VERIFICATION_TEMPERATURE", "0.0"))
        self.VERIFICATION_MAX_TOKENS: int = int(os.getenv("VERIFICATION_MAX_TOKENS", "200"))

        # Embedding Configuration (for RetrieverBuilder)
        self.EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

        # Retriever Configuration
        self.CHROMA_DB_PATH: str = os.getenv("CHROMA_DB_PATH", "./chroma_db")
        self.VECTOR_SEARCH_K: int = int(os.getenv("VECTOR_SEARCH_K", "5"))
        # Hybrid retriever weights: [vector_weight, bm25_weight]
        self.HYBRID_RETRIEVER_WEIGHTS: list = [0.5, 0.5]

        # Cache Configuration
        self.CACHE_DIR: Path = Path(os.getenv("CACHE_DIR", "./cache"))
        self.CACHE_EXPIRE_DAYS: int = int(os.getenv("CACHE_EXPIRE_DAYS", "7"))

        # Validate required settings
        if not self.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY environment variable is required. "
                "Please set it in your .env file or environment."
            )

    def __repr__(self) -> str:
        return f"Settings(model={self.OPENAI_MODEL}, temperature={self.OPENAI_TEMPERATURE})"


# Global settings instance
settings = Settings()
