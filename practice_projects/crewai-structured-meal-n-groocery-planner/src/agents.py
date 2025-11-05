from crewai import Agent
from crewai_tools import SerperDevTool


def create_meal_planner(llm):
    """Creates the Meal Planner agent."""
    return Agent(
        role="Meal Planner & Recipe Researcher",
        goal="Search for optimal recipes and create detailed meal plans",
        backstory="A skilled meal planner who researches the best recipes online, considering dietary needs, cooking skill levels, and budget constraints.",
        tools=[SerperDevTool()],
        llm=llm,
        verbose=False
    )


def create_shopping_organizer(llm):
    """Creates the Shopping Organizer agent."""
    return Agent(
        role="Shopping Organizer",
        goal="Organize grocery lists by store sections efficiently",
        backstory="An experienced shopper who knows how to organize lists for quick store trips and considers dietary restrictions.",
        tools=[],
        llm=llm,
        verbose=False
    )


def create_budget_advisor(llm):
    """Creates the Budget Advisor agent."""
    return Agent(
        role="Budget Advisor",
        goal="Provide cost estimates and money-saving tips",
        backstory="A budget-conscious shopper who helps families save money on groceries while respecting dietary needs.",
        tools=[SerperDevTool()],
        llm=llm,
        verbose=False
    )


def create_summary_agent(llm):
    """Creates the Report Compiler agent."""
    return Agent(
        role="Report Compiler",
        goal="Compile comprehensive meal planning reports from all team outputs",
        backstory="A skilled coordinator who organizes information from multiple specialists into comprehensive, easy-to-follow reports.",
        tools=[],
        llm=llm,
        verbose=False
    )