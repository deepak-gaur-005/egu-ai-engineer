import os
from pathlib import Path
from pyexpat.errors import messages
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key kaha hai ladleee")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"

#structue it
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f""" Extrct the personal information from the ticket strictly based on this schema and give a json output.{schema}"""

message_system={
    "role": "system",
    "content": system_prompt
}


text="Hello My name is habibi. Yesterday I broke up with my girlfriend sheetal I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"
prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""

# message me role an dcontent chahiye
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

response=client.chat.completions.create(model=model, messages=messages, response_format=response_format)
# print(response)
#print("#########################################")

answer=response.choices[0].message.content
print(answer)


#isko padhte kaise hey
import json
raw_json=answer
data_files=json.loads(raw_json)
ticket=Ticket(**data_files)


print(ticket.name)
print(ticket.email)
print(ticket.issue)