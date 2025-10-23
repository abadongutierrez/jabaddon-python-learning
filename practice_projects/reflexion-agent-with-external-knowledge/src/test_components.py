"""Test individual components: LLM, prompts, tools, and chains.

This script demonstrates and tests the basic building blocks of the reflexion agent
before they are integrated into the full graph.
"""

from langchain_core.messages import HumanMessage
from reflexion_agent_with_external_knowledge import (
    llm,
    tavily_tool,
    first_responder_prompt,
    initial_chain,
    revisor_chain,
    execute_tools,
)


def test_tavily_search():
    """Test the Tavily search tool."""
    print("="*80)
    print("TEST 1: Tavily Search Tool")
    print("="*80)

    sample_query = "healthy breakfast recipes"
    search_results = tavily_tool.run(sample_query)
    print(f"Search results for query '{sample_query}':\n{search_results}\n")


def test_llm_simple():
    """Test simple LLM response without structured output."""
    print("="*80)
    print("TEST 2: Simple LLM Response")
    print("="*80)

    question = "Any ideas for a healthy breakfast"
    response = llm.invoke(question).content
    print(f"Question: {question}")
    print(f"Response:\n{response}\n")


def test_prompt_chain():
    """Test the prompt chain with unstructured output."""
    print("="*80)
    print("TEST 3: Prompt Chain (Unstructured)")
    print("="*80)

    question = "Any ideas for a healthy breakfast"
    temp_chain = first_responder_prompt | llm
    response = temp_chain.invoke({"messages": [HumanMessage(content=question)]})
    print(f"Question: {question}")
    print(f"Response:\n{response.content}\n")


def test_initial_chain_structured():
    """Test the initial chain with structured output (tool calls)."""
    print("="*80)
    print("TEST 4: Initial Chain (Structured Output)")
    print("="*80)

    question = "Any ideas for a healthy breakfast"
    response = initial_chain.invoke({"messages": [HumanMessage(question)]})

    print(f"Question: {question}\n")
    print("Full Structured Output:")
    print(response.tool_calls)
    print()

    if response.tool_calls:
        answer_content = response.tool_calls[0]['args']['answer']
        print("Initial Answer:")
        print(answer_content)
        print()

        reflection_content = response.tool_calls[0]['args']['reflection']
        print("Reflection:")
        print(reflection_content)
        print()

        search_queries = response.tool_calls[0]['args']['search_queries']
        print("Search Queries:")
        for i, query in enumerate(search_queries, 1):
            print(f"  {i}. {query}")
        print()


def test_execute_tools():
    """Test the execute_tools function that runs search queries."""
    print("="*80)
    print("TEST 5: Execute Tools Function")
    print("="*80)

    question = "Any ideas for a healthy breakfast"
    response = initial_chain.invoke({"messages": [HumanMessage(question)]})

    response_list = [
        HumanMessage(content=question),
        response
    ]

    print(f"Question: {question}\n")
    print("Executing search queries from the initial response...")

    tool_response = execute_tools({"messages": response_list})

    print("\nTool Responses:")
    for tool_msg in tool_response["messages"]:
        print(f"Tool Call ID: {tool_msg.tool_call_id}")
        print(f"Content preview: {tool_msg.content[:200]}...")
        print()


def test_revisor_chain():
    """Test the revisor chain that revises answers based on search results."""
    print("="*80)
    print("TEST 6: Revisor Chain")
    print("="*80)

    question = "Any ideas for a healthy breakfast"

    # Get initial response
    response = initial_chain.invoke({"messages": [HumanMessage(question)]})

    # Build message list
    response_list = [
        HumanMessage(content=question),
        response
    ]

    # Execute tools
    tool_response = execute_tools({"messages": response_list})
    response_list.extend(tool_response["messages"])

    # Get revised response
    revised_response = revisor_chain.invoke({"messages": response_list})

    print(f"Question: {question}\n")
    print("Revised Answer with References:")
    if revised_response.tool_calls:
        revised_args = revised_response.tool_calls[0]['args']
        print(f"\nAnswer:\n{revised_args['answer']}\n")
        print(f"Reflection:\n{revised_args['reflection']}\n")
        print("References:")
        for i, ref in enumerate(revised_args.get('references', []), 1):
            print(f"  [{i}] {ref}")
        print()


if __name__ == "__main__":
    print("\n" + "="*80)
    print("REFLEXION AGENT - COMPONENT TESTS")
    print("="*80 + "\n")

    # Run all tests
    test_tavily_search()
    test_llm_simple()
    test_prompt_chain()
    test_initial_chain_structured()
    test_execute_tools()
    test_revisor_chain()

    print("="*80)
    print("ALL COMPONENT TESTS COMPLETED")
    print("="*80)
