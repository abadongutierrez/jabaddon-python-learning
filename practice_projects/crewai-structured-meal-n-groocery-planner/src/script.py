import os
from crewai import LLM, Crew, Process
from agents import (
    create_meal_planner,
    create_shopping_organizer,
    create_budget_advisor,
    create_summary_agent
)
from leftover import LeftoversCrew
from tasks import (
    create_meal_planning_task,
    create_shopping_task,
    create_budget_task,
    create_summary_task
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

budget_advisor = create_budget_advisor(llm)
budget_task = create_budget_task(budget_advisor, [meal_planning_task, shopping_task])

leftovers_cb = LeftoversCrew(llm=llm)
yaml_leftover_manager = leftovers_cb.leftover_manager()
yaml_leftover_task    = leftovers_cb.leftover_task()

summary_agent = create_summary_agent(llm)
summary_task = create_summary_task(summary_agent, [meal_planning_task, shopping_task, budget_task, yaml_leftover_task])

complete_grocery_crew = Crew(
    agents=[
        meal_planner,           
        shopping_organizer,      
        budget_advisor,         
        yaml_leftover_manager,  # YAML-based leftover manager
        summary_agent           # New summary agent
    ],
    tasks=[
        meal_planning_task,     
        shopping_task,          
        budget_task,            
        yaml_leftover_task,    # YAML-based leftover task
        summary_task            # New summary task
    ],
    process=Process.sequential,
    verbose=True
)

# Run the complete crew
complete_result = complete_grocery_crew.kickoff(
    inputs={
        "meal_name": "Chicken Stir Fry",
        "servings": 4,
        "budget": "$25",
        "dietary_restrictions": ["no nuts", "low sodium"],
        "cooking_skill": "beginner"
    }
)

print("✅ Complete meal planning with summary completed!")
print("📋 Complete Results:")
print(complete_result)