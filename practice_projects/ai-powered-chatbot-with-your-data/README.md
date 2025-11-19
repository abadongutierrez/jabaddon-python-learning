# AI-Powered Chatbot with Your Data

A RAG (Retrieval-Augmented Generation) based chatbot that answers questions about PDF documents using LangChain, Ollama, and ChromaDB.

## Features

- PDF document processing and indexing
- Vector embeddings using Ollama
- Retrieval-Augmented Generation (RAG) for accurate answers
- Command-line interface for easy interaction
- Chat history tracking

## Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.13+**
2. **Poetry** (Python package manager)
3. **Ollama** (Local LLM runtime)

### Installing Ollama

Install Ollama from [ollama.ai](https://ollama.ai):

```bash
# macOS
brew install ollama

# Start Ollama service
ollama serve
```

### Pull Required Models

```bash
# Pull the LLM model
ollama pull llama3.2:latest

# Pull the embedding model
ollama pull all-minilm:latest
```

## Installation

1. Clone the repository and navigate to the project directory

2. Install dependencies using Poetry:

```bash
poetry install
```

## Usage

### Basic Usage

Run the script with a question about your PDF:

```bash
poetry run python src/script.py "Your question here"
```

### Examples

```bash
# Ask a question about info.pdf (default)
poetry run python src/script.py "Cuanto hay que pagar?"

# Specify a different PDF file
poetry run python src/script.py "What is the main topic?" --pdf "document.pdf"

# Get help
poetry run python src/script.py --help
```

### Command-Line Arguments

- `question` (required): The question to ask about the PDF document
- `--pdf` (optional): Path to the PDF file (default: `info.pdf`)
