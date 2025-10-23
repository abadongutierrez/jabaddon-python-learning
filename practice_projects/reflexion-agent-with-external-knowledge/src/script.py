"""Main script for the Reflexion Agent.

This is a deep research agent that uses a technique called reflection.
It's designed to:
1. Answer a question
2. Critique its own answer
3. Identify weaknesses
4. Use tools to find more information
5. Revise its answer to be more accurate and complete

Usage:
    python script.py                    # Run with default question
    python -m test_components           # Test individual components
    python -m test_graph                # Test the full graph workflow
"""

import sys
from langchain_core.messages import HumanMessage
from reflexion_agent_with_external_knowledge import app


def run_reflexion_agent(question: str) -> dict:
    """Run the reflexion agent on a question.

    Args:
        question: The question to answer

    Returns:
        The complete state with all messages
    """
    print("="*80)
    print("REFLEXION AGENT")
    print("="*80)
    print(f"\nQuestion: {question}\n")
    print("Processing...\n")

    response_state = app.invoke({
        "messages": [HumanMessage(content=question)]
    })

    return response_state


def display_results(response_state: dict):
    """Display the results from the reflexion agent.

    Args:
        response_state: The state returned by the agent
    """
    messages = response_state["messages"]

    # Extract all answers
    answers = []
    for msg in reversed(messages):
        if getattr(msg, 'tool_calls', None):
            for tool_call in msg.tool_calls:
                answer = tool_call.get('args', {}).get('answer')
                if answer:
                    answers.append({
                        'answer': answer,
                        'reflection': tool_call.get('args', {}).get('reflection'),
                        'references': tool_call.get('args', {}).get('references', [])
                    })

    # Display initial answer
    print("="*80)
    print("INITIAL DRAFT ANSWER")
    print("="*80)
    if len(answers) > 0:
        initial = answers[-1]
        print(initial['answer'])
        print()

    # Display final answer
    print("="*80)
    print(f"FINAL REVISED ANSWER (after {len(answers) - 1} iterations)")
    print("="*80)
    if len(answers) > 0:
        final = answers[0]
        print(final['answer'])

        if final.get('references'):
            print("\nReferences:")
            for i, ref in enumerate(final['references'], 1):
                print(f"  [{i}] {ref}")
        print()


def main():
    """Main entry point."""
    # Default question
    default_question = """I'm pre-diabetic and need to lower my blood sugar, and I have heart issues.
    What breakfast foods should I eat and avoid?"""

    # Allow custom question from command line
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
    else:
        question = default_question

    # Run the agent
    response_state = run_reflexion_agent(question)

    # Display results
    display_results(response_state)

    print("="*80)
    print("For more detailed tests, run:")
    print("  python test_components.py  # Test individual components")
    print("  python test_graph.py       # Test graph workflow")
    print("="*80)


if __name__ == "__main__":
    main()