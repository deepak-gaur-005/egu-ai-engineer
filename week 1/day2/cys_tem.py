import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key kaha hai ladleee")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"
prompt="when u resign from the post of pm of india"
#system
message_system={
    "role": "system",
    "content": "You are modi"
}

# message me role an content chahiye
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]

# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, temperature=2)
#print(response)

print("#########################################")
answer=response.choices[0].message.content
print(answer)
