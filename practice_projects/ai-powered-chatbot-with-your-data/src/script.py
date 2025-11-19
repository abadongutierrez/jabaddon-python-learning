import sys
import argparse
from pathlib import Path
from worker import init_llm, process_document, process_prompt

# Initialize chat history
import worker
worker.chat_history = []

def main():
    """Main function to process PDF and answer questions"""

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='RAG-based PDF question answering using LangChain and Ollama')
    parser.add_argument('question', type=str, help='Question to ask about the PDF document')
    parser.add_argument('--pdf', type=str, default='document.pdf', help='Path to the PDF file (default: info.pdf)')

    args = parser.parse_args()

    # Initialize the LLM and embeddings
    print("Initializing LLM and embeddings...")
    init_llm()
    print("✓ LLM initialized\n")

    # Path to the PDF file
    pdf_path = args.pdf

    # Check if PDF exists
    if not Path(pdf_path).exists():
        print(f"Error: PDF file '{pdf_path}' not found!")
        print(f"Please ensure '{pdf_path}' exists in the current directory.")
        return

    # Process the PDF document
    print(f"Processing document: {pdf_path}")
    process_document(pdf_path)
    print("✓ Document processed and indexed\n")

    # Ask the question
    question = args.question
    print(f"Question: {question}")
    print("-" * 50)

    # Get the answer
    answer = process_prompt(question)
    print(f"Answer: {answer}")
    print("-" * 50)

if __name__ == "__main__":
    main()
