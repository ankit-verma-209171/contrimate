from contrimate_agent.agent import Person

person = Person(name="Alice", age=30).model_dump_json()
print(person)