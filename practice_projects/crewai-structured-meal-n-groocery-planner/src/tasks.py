from crewai import Task
from models import MealPlan, GroceryShoppingPlan

def create_meal_planning_task(agent):
    """Creates the meal planning task."""
    return Task(
        description=(
            "Search for the best '{meal_name}' recipe for {servings} people within a {budget} budget. "
            "Consider dietary restrictions: {dietary_restrictions} and cooking skill level: {cooking_skill}. "
            "Find recipes that match the skill level and provide complete ingredient lists with quantities."
        ),
        expected_output="A detailed meal plan with researched ingredients, quantities, and cooking instructions appropriate for the skill level.",
        agent=agent,
        output_pydantic=MealPlan,
        output_file="meals.json"
    )


def create_shopping_task(agent, context):
    """Creates the shopping list organization task."""
    return Task(
        description=(
            "Organize the ingredients from the '{meal_name}' meal plan into a grocery shopping list. "
            "Group items by store sections and estimate quantities for {servings} people. "
            "Consider dietary restrictions: {dietary_restrictions} and cooking skill: {cooking_skill}. "
            "Stay within budget: {budget}."
        ),
        expected_output="An organized shopping list grouped by store sections with quantities and prices.",
        agent=agent,
        context=context,
        output_pydantic=GroceryShoppingPlan,
        output_file="shopping_list.json"
    )


def create_budget_task(agent, context):
    """Creates the budget analysis task."""
    return Task(
        description=(
            "Analyze the shopping plan for '{meal_name}' serving {servings} people. "
            "Ensure total cost stays within {budget}. Consider dietary restrictions: {dietary_restrictions}. "
            "Provide practical money-saving tips and alternative ingredients if needed to meet budget."
        ),
        expected_output="A complete shopping guide with detailed prices, budget analysis, and money-saving tips.",
        agent=agent,
        context=context,
        output_file="shopping_guide.md"
    )


def create_summary_task(agent, context):
    """Creates the summary and report compilation task."""
    return Task(
        description=(
            "Compile a comprehensive meal planning report that includes:\n"
            "1. The complete recipe and cooking instructions from the meal planner\n"
            "2. The organized shopping list with prices from the shopping organizer\n"
            "3. The budget analysis and money-saving tips from the budget advisor\n"
            "4. The leftover management suggestions from the waste reduction specialist\n"
            "Format this as a complete, user-friendly meal planning guide."
        ),
        expected_output="A comprehensive meal planning guide that combines all team outputs into one cohesive report.",
        agent=agent,
        context=context,
    )
