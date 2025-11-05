import os
from crewai import Crew, Process
from crewai import LLM
from agents import (
    create_meal_planner,
    create_shopping_organizer
)
from tasks import (
    create_meal_planning_task,
    create_shopping_task
)

# Initialize the LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_STUDIO_API_KEY"),
    temperature=0.7
)

meal_planner = create_meal_planner(llm)
meal_planning_task = create_meal_planning_task(meal_planner)

shopping_organizer = create_shopping_organizer(llm)
shopping_task = create_shopping_task(shopping_organizer, [meal_planning_task])

two_agent_grocery_crew = Crew(
    agents=[meal_planner, shopping_organizer],  # Both agents
    tasks=[meal_planning_task, shopping_task],   # Both tasks
    process=Process.sequential,
    verbose=True
)

# Run the complete crew (this will do BOTH meal planning AND shopping)
shopping_result = two_agent_grocery_crew.kickoff(
    inputs={
        "meal_name": "Chicken Stir Fry",
        "servings": 4,
        "budget": "$25",                           
        "dietary_restrictions": ["no nuts"],      
        "cooking_skill": "beginner"               
    }
)

# Print the shopping results
print("✅ Complete meal planning + shopping completed!")
print("📋 Shopping Results:")
print(shopping_result)