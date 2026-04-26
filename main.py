from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def generate_test_cases(req):
    prompt =f"""act as a qa engineer.
    create test cases for:
    {req}

    include positive, negative edge cases"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content":prompt}]
    )

    return response.choices[0].message.content

print(generate_test_cases("User Login with OTP"))
