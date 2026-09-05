from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq

load_dotenv()  # Load environment variables from .env file

llm = ChatGroq(
    model="qwen/qwen3.6-27b", temperature=0.7
)  # Initialize the Groq model

response = llm.invoke("What is the meaning of life?")  # Invoke the model with a prompt
print(response.content)  # Print the response from the model
