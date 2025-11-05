import os
from crewai import Crew, Process
from crewai import LLM
from agents import (
    create_meal_planner
)
from tasks import (
    create_meal_planning_task
)


# Initialize the LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_STUDIO_API_KEY"),
    temperature=0.7
)

meal_planner = create_meal_planner(llm)
meal_planning_task = create_meal_planning_task(meal_planner)

meal_planner_crew = Crew(
    agents=[meal_planner],
    tasks=[meal_planning_task],
    process=Process.sequential,  # Ensures tasks are executed in order
    verbose=True
)

meal_planner_result = meal_planner_crew.kickoff(
    inputs={
        "meal_name": "Chicken Stir Fry",
        "servings": 4,
        "budget": "$25",                           
        "dietary_restrictions": ["no nuts"],       
        "cooking_skill": "beginner"                
    }
)
print("✅ Single meal planning completed!")
print("📋 Single Meal Results:")
print(meal_planner_result)