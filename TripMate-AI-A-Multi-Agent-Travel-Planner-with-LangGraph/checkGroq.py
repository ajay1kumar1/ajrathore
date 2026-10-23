import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # Loads variables from a .env file if you have one

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    api_key=os.environ.get("GROQ_API_KEY"),
)
print(" result", llm)