from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(encoding='utf8')

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

role_description = ""
with open('RoleDescription.txt') as file:
    role_description = file.read()

query = input("What kinds of cards do you want to find?")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  messages=[
    {"role": "system", "content": role_description},
    {"role": "user", "content": query}
  ]
)

print(completion.choices[0].message)