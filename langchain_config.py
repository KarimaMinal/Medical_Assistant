import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq 

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),  
    model_name="llama3-8b-8192",        
    temperature=0.3,
)
