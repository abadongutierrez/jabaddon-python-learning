from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage
from typing import Literal
import json

class WeatherSchema(BaseModel):
    condition: str = Field(description="Weather condition such as sunny, rainy, cloudy")
    temperature: int = Field(description="Temperature value")
    unit: str = Field(description="Unit of temperature, e.g., Celsius or Fahrenheit")

llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

weather_llm = llm.bind_tools(tools=[WeatherSchema])
response = weather_llm.invoke("It's sunny and 75 degrees")
print(response.tool_calls)

class SpamSchema(BaseModel):
    classification: str = Field(description="Email classification: spam or not spam")
    confidence: float = Field(description="Confidence score between 0 and 1")
    reason: str = Field(description="Reason for classification")

spam_llm = llm.bind_tools(tools=[SpamSchema])
response = spam_llm.invoke("Congratulations! You've won a free lottery ticket.")
print(response.tool_calls)

class Add(BaseModel):
    """ Adds two numbers together. """
    a: int = Field(description="The first number to add")
    b: int = Field(description="The second number to add")

add_llm = llm.bind_tools(tools=[Add])

question = "add 1 and 10"
response = add_llm.invoke([HumanMessage(content=question)])
print(response.tool_calls)

def extract_and_add(response):
    tool_call = response.tool_calls[0]
    a = tool_call['args']['a']
    b = tool_call['args']['b']
    return a + b

result = extract_and_add(response)
print(f"The result of adding is: {result}")

class TwoOperands(BaseModel):
    """ Represents two operands for an operation. """
    a: float = Field(description="The first operand")
    b: float = Field(description="The second operand")

# The Literal type from Python's typing module restricts a variable to one or more specific constant values

class AddInput(TwoOperands):
    """ Input schema for addition operation. """
    operation: Literal["add"] = Field(description="The operation to perform, must be 'add'")

class SubtractInput(TwoOperands):
    """ Input schema for subtraction operation. """
    operation: Literal["subtract"] = Field(description="The operation to perform, must be 'subtract'")

class MathOutput(BaseModel):
    """ Represents the result of a mathematical operation. """
    result: float = Field(description="The result of the operation")

def add_tool(data: AddInput) -> MathOutput:
    """ Performs addition of two numbers. """
    return MathOutput(result=data.a + data.b)

def subtract_tool(data: SubtractInput) -> MathOutput:
    """ Performs subtraction of two numbers. """
    return MathOutput(result=data.a - data.b)

def dispatch_tool(json_payload: str) -> str:
    """ Dispatches the tool call to the appropriate function based on the operation. """
    data = json.loads(json_payload)
    operation = data.get("operation")

    if operation == "add":
        output = add_tool(AddInput.parse_raw(json_payload))
    elif operation == "subtract":
        output = subtract_tool(SubtractInput.parse_raw(json_payload))
    else:
        raise ValueError("Unsupported operation")
    return output.json()

result_json = dispatch_tool('{"a": 5, "b": 3, "operation": "add"}')
print(f"Dispatch result: {result_json}")

class CalculatorSchema(TwoOperands):
    operation: Literal["add", "subtract", "multiply", "divide"] = Field(
        description="The operation to perform"
    )
    a: float = Field(description="The first operand")
    b: float = Field(description="The second operand")

calculator_llm = llm.bind_tools(tools=[CalculatorSchema])

response = calculator_llm.invoke("What is 10 minus 4?")
print(response.tool_calls)

response = calculator_llm.invoke("Multiply 7 by 8")
print(response.tool_calls)
