import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_answer(
        query,
        retrieved_docs
):

    context = "\n\n".join(
        [
            doc["content"]
            for doc in retrieved_docs
        ]
    )

    prompt = f"""
Answer ONLY using the provided context.

Context:
{context}

Question:
{query}

If the answer is not present in the context,
say:
'I could not find this information.'

Provide a concise answer.
"""

    response = model.generate_content(
        prompt
    )

    return response.text