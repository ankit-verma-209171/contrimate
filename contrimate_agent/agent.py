from google.adk.agents import Agent
from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


def get_persons() -> dict[str, list[str]]:
    """
    Retrieve a list of persons as JSON-serializable dictionaries.

    Returns:
        dict: A dictionary with a single key "people", whose value is a list of JSON strings,
            each representing a Person object.
    Example:
        {
            "people": [
                '{"name": "Alice", "age": 30}',
                '{"name": "Bob", "age": 25}'
        }
    """
    people = [
        Person(name="Alice", age=30),
        Person(name="Bob", age=25),
        Person(name="Charlie", age=35),
    ]
    return {"people": [person.model_dump_json() for person in people]}


def get_count(string: str) -> dict[str, int]:
    """
    Count the number of characters in a given string.
    Args:
        string (str): The input string to count characters in.
    Returns:
        dict: A dictionary with a single key "count", whose value is the number of characters
            in the input string.
    Example:
        {
            "count": 13
        }
    """
    return {"count": len(string)}


root_agent = Agent(
    name="person_agent",
    model="gemini-2.0-flash",
    description="An agent that can interact with and provide information about people.",
    instruction="Use this agent to get information about different persons.",
    tools=[get_persons, get_count],
)
