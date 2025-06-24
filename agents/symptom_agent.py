from langchain.prompts import PromptTemplate
from langchain_config import llm

def analyze_symptoms(symptoms: str) -> str:
    prompt = PromptTemplate.from_template(
        "Given these symptoms: {symptoms}, what is the most likely diagnosis?"
    )
    return llm.predict(prompt.format(symptoms=symptoms))
