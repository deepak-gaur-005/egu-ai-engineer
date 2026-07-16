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

#3 prompt
prompt1="who is haland"
prompt2="what is the capital of france"
prompt3="how to make a cake"

promts=[prompt1,prompt2,prompt3]

for prompt in promts:
    message={
        "role": role,
        "content": prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage=response.usage
    print(f"Prompt: {prompt} -->your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")

# message me role an dcontent chahiye
# message={
#     "role": role,
#     "content": prompt
# }

# messages=[message]

# response=client.chat.completions.create(model=model, messages=messages)
# print(response)

# print("#########################################")
# answer=response.choices[0].message.content
# print(answer)
