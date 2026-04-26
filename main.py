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

    includes:
    1.positive
    2.negative 
    3.edge cases"""

    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role":"user", "content":prompt}]
    # )

    return llm.invoke(prompt)


def bug_analyzer(bug):
    prompt = f"""
    act as a qa engineer
    analyzing this bug:{bug}

    give:
    1. bug type
    2. severity
    3. possible root cause
    4. reprodcution steps 
    """

    return llm.invoke(prompt)

def qa_agent(task, text):
    if task.lower() == "test":
        return generate_test_cases(text)
    elif task.lower() == "bug":
        return bug_analyzer(text)
    else:
        return "unknown task!!"

print(qa_agent("test","User Login with OTP"))