from openai import OpenAI
from typing import Dict, List
from langchain.schema import Document
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)


class ResearchAgent:
    def __init__(self):
        """
        Initialize the research agent with the OpenAI client.
        """
        logger.info("Initializing ResearchAgent with OpenAI...")
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.RESEARCH_MODEL
        self.temperature = settings.RESEARCH_TEMPERATURE
        self.max_tokens = settings.RESEARCH_MAX_TOKENS
        logger.info(f"ResearchAgent initialized successfully with model: {self.model}")

    def sanitize_response(self, response_text: str) -> str:
        """
        Sanitize the LLM's response by stripping unnecessary whitespace.
        """
        return response_text.strip()

    def generate_prompt(self, question: str, context: str) -> str:
        """
        Generate a structured prompt for the LLM to generate a precise and factual answer.
        """
        prompt = f"""
        You are an AI assistant designed to provide precise and factual answers based on the given context.

        **Instructions:**
        - Answer the following question using only the provided context.
        - Be clear, concise, and factual.
        - Return as much information as you can get from the context.

        **Question:** {question}
        **Context:**
        {context}

        **Provide your answer below:**
        """
        return prompt

    def generate(self, question: str, documents: List[Document]) -> Dict:
        """
        Generate an initial answer using the provided documents.
        """
        logger.info(f"ResearchAgent.generate called with question='{question}' and {len(documents)} documents.")

        # Combine the top document contents into one string
        context = "\n\n".join([doc.page_content for doc in documents])
        logger.debug(f"Combined context length: {len(context)} characters.")

        # Create a prompt for the LLM
        prompt = self.generate_prompt(question, context)
        logger.debug("Prompt created for the LLM.")

        # Call the OpenAI LLM to generate the answer
        try:
            logger.info("Sending prompt to OpenAI model...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens
            )
            logger.info("OpenAI response received.")
        except Exception as e:
            logger.error(f"Error during OpenAI API call: {e}")
            raise RuntimeError("Failed to generate answer due to an OpenAI API error.") from e

        # Extract and process the LLM's response
        try:
            llm_response = response.choices[0].message.content.strip()
            logger.debug(f"Raw LLM response:\n{llm_response}")
        except (IndexError, AttributeError) as e:
            logger.error(f"Unexpected response structure: {e}")
            llm_response = "I cannot answer this question based on the provided documents."

        # Sanitize the response
        draft_answer = self.sanitize_response(llm_response) if llm_response else "I cannot answer this question based on the provided documents."

        logger.info(f"Generated answer: {draft_answer}")

        return {
            "draft_answer": draft_answer,
            "context_used": context
        }
