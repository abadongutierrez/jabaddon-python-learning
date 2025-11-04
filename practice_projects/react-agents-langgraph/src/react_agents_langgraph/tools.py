import json
from langchain_tavily import TavilySearch
from langchain.tools import tool


# Initialize Tavily search tool
tavily_tool = TavilySearch(max_results=1)

@tool # decorator that creates a StructuredTool object
def search_tool(query: str) -> str:
    """Use Tavily to search the web for a query"""
    return tavily_tool.invoke(query)

@tool
def recommend_clothing(weather: str) -> str:
    """Recommend clothing based on the weather description."""
    weather = weather.lower()
    if "snow" in weather or "freezing" in weather:
        return "Wear a heavy coat, scarf, gloves, and waterproof boots."
    elif "rain" in weather or "wet" in weather:
        return "Wear a waterproof jacket and carry an umbrella, along with waterproof shoes."
    elif "hot" in weather or "85" in weather:
        return "T-shirt, shorts, and sandals are appropriate. Don't forget sunscreen!"
    elif "cold" in weather or "50" in weather:
        return "Wear a warm sweater or light jacket, along with long pants and closed-toe shoes."
    else:
        return "A light jacket or sweater with comfortable pants and shoes should be fine."
    
tools = [search_tool, recommend_clothing]

tools_by_name = {tool.name: tool for tool in tools}