import os
from crewai_tools import SerperDevTool
from crewai import LLM, Agent, Task, Crew, Process

# os.environ['SERPER_API_KEY'] = "API_KEY_HERE"

search_tool = SerperDevTool()
print(type(search_tool))

# Run a query
search_query = "Latest Breakthroughs in machine learning"
search_results = search_tool.run(query=search_query)

# Print the results
print(f"Search Results for '{search_results}':\n")

# Initialize the LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GOOGLE_STUDIO_API_KEY"),
    temperature=0.7
)

research_agent = Agent(
  role='Senior Research Analyst',
  goal='Uncover cutting-edge information and insights on any subject with comprehensive analysis',
  backstory="""You are an expert researcher with extensive experience in gathering, analyzing, and synthesizing information across multiple domains. 
  Your analytical skills allow you to quickly identify key trends, separate fact from opinion, and produce insightful reports on any topic. 
  You excel at finding reliable sources and extracting valuable information efficiently.""",
  verbose=True,
  allow_delegation=False,
  llm = llm,
  tools=[SerperDevTool()]
)

# Define your agents with roles and goals
# Define the Writer Agent
writer_agent = Agent(
  role='Tech Content Strategist',
  goal='Craft well-structured and engaging content based on research findings',
  backstory="""You are a skilled content strategist known for translating 
  complex topics into clear and compelling narratives. Your writing makes 
  information accessible and engaging for a wide audience.""",
  verbose=True,
  llm = llm,
  allow_delegation=True
)

research_task = Task(
  description="Analyze the major {topic}, identifying key trends and technologies. Provide a detailed report on their potential impact.",
  agent=research_agent,
  expected_output="A detailed report on {topic}, including trends, emerging technologies, and their impact."
)

writer_task = Task(
  description="Create an engaging blog post based on the research findings about {topic}. Tailor the content for a tech-savvy audience, ensuring clarity and interest.",
  agent=writer_agent,
  expected_output="A 4-paragraph blog post on {topic}, written clearly and engagingly for tech enthusiasts."
)

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    verbose=True 
)

result = crew.kickoff(inputs={"topic": "Latest Generative AI breakthroughs"})

type(result)

final_output = result.raw
print("Final output:", final_output)

tasks_outputs = result.tasks_output

print("Task Description", tasks_outputs[0].description)
print("Output of research task ",tasks_outputs[0])

print("Writer task description:", tasks_outputs[1].description)
print(" \nOutput of writer task:", tasks_outputs[1].raw)

print("We can get the agent for researcher task:  ",tasks_outputs[0].agent)
print("We can get the agent for the writer task: ",tasks_outputs[1].agent)

token_count = result.token_usage.total_tokens
prompt_tokens = result.token_usage.prompt_tokens
completion_tokens = result.token_usage.completion_tokens

print(f"Total tokens used: {token_count}")
print(f"Prompt tokens: {prompt_tokens} (used for instructions to the model)")
print(f"Completion tokens: {completion_tokens} (generated in response)")