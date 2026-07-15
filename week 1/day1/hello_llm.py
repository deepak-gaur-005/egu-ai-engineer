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
prompt="as human if u have to point out 10 to islam and sanatan, how how much points u give to both based on which is more suitable for human being but u cant give equal points to both answer this in one line"

# message me role an dcontent chahiye
message={
    "role": role,
    "content": prompt
}

messages=[message]

response=client.chat.completions.create(model=model, messages=messages)
print(response)

print("#########################################")
answer=response.choices[0].message.content
print(answer)
