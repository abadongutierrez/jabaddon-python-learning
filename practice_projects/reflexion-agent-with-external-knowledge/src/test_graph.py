"""Test the full reflexion agent graph.

This script demonstrates the complete reflexion agent workflow using LangGraph,
which orchestrates multiple iterations of answering, researching, and revising.
"""

from langchain_core.messages import HumanMessage
from reflexion_agent_with_external_knowledge import app, MAX_ITERATIONS


def print_message_summary(messages):
    """Print a summary of message types in the state."""
    from langchain_core.messages import ToolMessage, AIMessage

    ai_count = sum(1 for msg in messages if isinstance(msg, AIMessage))
    tool_count = sum(1 for msg in messages if isinstance(msg, ToolMessage))
    human_count = sum(1 for msg in messages if isinstance(msg, HumanMessage))

    print(f"Message Summary:")
    print(f"  - Human messages: {human_count}")
    print(f"  - AI messages: {ai_count}")
    print(f"  - Tool messages: {tool_count}")
    print(f"  - Total messages: {len(messages)}")
    print()


def extract_answers(messages):
    """Extract all answers from the message history."""
    answers = []

    # Loop through all messages in reverse to find all tool_calls with answers
    for msg in reversed(messages):
        if getattr(msg, 'tool_calls', None):
            for tool_call in msg.tool_calls:
                answer = tool_call.get('args', {}).get('answer')
                if answer:
                    answers.append({
                        'answer': answer,
                        'reflection': tool_call.get('args', {}).get('reflection'),
                        'search_queries': tool_call.get('args', {}).get('search_queries', []),
                        'references': tool_call.get('args', {}).get('references', [])
                    })

    return answers


def test_simple_question():
    """Test the graph with a simple question."""
    print("="*80)
    print("TEST 1: Simple Question")
    print("="*80)

    question = "What are the best foods for a healthy breakfast?"

    print(f"Question: {question}\n")
    print(f"Running graph (max {MAX_ITERATIONS} iterations)...\n")

    response_state = app.invoke({
        "messages": [HumanMessage(content=question)]
    })

    messages = response_state["messages"]

    print_message_summary(messages)

    # Extract and display answers
    answers = extract_answers(messages)

    print("\n" + "-"*80)
    print("INITIAL DRAFT ANSWER")
    print("-"*80)
    if len(answers) > 0:
        initial = answers[-1]  # Last in list is the first answer
        print(initial['answer'])
        print()

    print("-"*80)
    print(f"REVISION HISTORY ({len(answers) - 1} revisions)")
    print("-"*80)
    for i, ans in enumerate(answers[:-1][::-1], 1):  # Reverse to show in chronological order
        print(f"\nRevision {i}:")
        print(ans['answer'])
        if ans.get('references'):
            print("\nReferences:")
            for j, ref in enumerate(ans['references'], 1):
                print(f"  [{j}] {ref}")
        print()


def test_complex_question():
    """Test the graph with a more complex, medical question."""
    print("\n" + "="*80)
    print("TEST 2: Complex Medical Question")
    print("="*80)

    question = """I'm pre-diabetic and need to lower my blood sugar, and I have heart issues.
    What breakfast foods should I eat and avoid?"""

    print(f"Question: {question}\n")
    print(f"Running graph (max {MAX_ITERATIONS} iterations)...\n")

    response_state = app.invoke({
        "messages": [HumanMessage(content=question)]
    })

    messages = response_state["messages"]

    print_message_summary(messages)

    # Extract and display answers
    answers = extract_answers(messages)

    print("\n" + "-"*80)
    print("INITIAL DRAFT ANSWER")
    print("-"*80)
    if len(answers) > 0:
        initial = answers[-1]
        print(initial['answer'])
        print("\nInitial Reflection:")
        print(f"  Missing: {initial['reflection'].get('missing', 'N/A')}")
        print(f"  Superfluous: {initial['reflection'].get('superfluous', 'N/A')}")
        print("\nSearch Queries Generated:")
        for j, query in enumerate(initial['search_queries'], 1):
            print(f"  {j}. {query}")
        print()

    print("-"*80)
    print(f"FINAL REVISED ANSWER (after {len(answers) - 1} iterations)")
    print("-"*80)
    if len(answers) > 0:
        final = answers[0]  # First in reversed list is the final answer
        print(final['answer'])
        if final.get('references'):
            print("\nReferences:")
            for j, ref in enumerate(final['references'], 1):
                print(f"  [{j}] {ref}")
        print()


def test_show_all_iterations():
    """Show detailed view of all iterations."""
    print("\n" + "="*80)
    print("TEST 3: Detailed Iteration View")
    print("="*80)

    question = "Should I eat eggs for breakfast if I have high cholesterol?"

    print(f"Question: {question}\n")
    print(f"Running graph (max {MAX_ITERATIONS} iterations)...\n")

    response_state = app.invoke({
        "messages": [HumanMessage(content=question)]
    })

    messages = response_state["messages"]

    print_message_summary(messages)

    # Extract and display all answers with full details
    answers = extract_answers(messages)

    for i, ans in enumerate(reversed(answers), 1):
        iteration_label = "INITIAL ANSWER" if i == 1 else f"REVISION {i - 1}"

        print("\n" + "-"*80)
        print(iteration_label)
        print("-"*80)

        print(f"\nAnswer:\n{ans['answer']}\n")

        print("Reflection:")
        print(f"  Missing: {ans['reflection'].get('missing', 'N/A')}")
        print(f"  Superfluous: {ans['reflection'].get('superfluous', 'N/A')}")

        if ans['search_queries']:
            print("\nSearch Queries:")
            for j, query in enumerate(ans['search_queries'], 1):
                print(f"  {j}. {query}")

        if ans.get('references'):
            print("\nReferences:")
            for j, ref in enumerate(ans['references'], 1):
                print(f"  [{j}] {ref}")

        print()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("REFLEXION AGENT - GRAPH TESTS")
    print("="*80 + "\n")

    # Run all tests
    test_simple_question()
    test_complex_question()
    test_show_all_iterations()

    print("\n" + "="*80)
    print("ALL GRAPH TESTS COMPLETED")
    print("="*80)
