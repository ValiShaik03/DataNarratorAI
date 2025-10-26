import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_insights(df):
    desc = df.describe(include="all").to_string()
    prompt = f"""
    You are a data analyst. Analyze the following dataset summary and generate 5 key insights in plain English:
    {desc}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250
    )

    return response.choices[0].message.content
