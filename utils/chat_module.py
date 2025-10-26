import os
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_data(df, query):
    prompt = f"""
    You are a data assistant. Answer based on this dataset:
    {df.head(10).to_string(index=False)}
    Question: {query}
    Provide the answer clearly and concisely.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )

    return response.choices[0].message.content
