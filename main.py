from openai import OpenAI
import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()
# client = OpenAI()
llm = Ollama(model='llama3')


def generate_test_cases(req):
    prompt =f"""act as a qa engineer.
    create test cases for:
    {req}

    include positive, negative edge cases"""

    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role":"user", "content":prompt}]
    # )

    response = llm.invoke(prompt)

    return response

print(generate_test_cases("User Login with OTP"))