from langchain.prompts import PromptTemplate
from langchain_config import llm

def get_safety_advice(diagnosis: str) -> str:
    prompt = PromptTemplate.from_template(
        "Give safety precautions and advice for someone diagnosed with: {diagnosis}."
    )
    return llm.predict(prompt.format(diagnosis=diagnosis))
