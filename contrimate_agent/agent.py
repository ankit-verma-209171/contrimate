from google.adk.agents import Agent


root_agent = Agent(
    name="calculator_agent",
    model="gemini-2.0-flash",
    description="An agent that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.",
)
