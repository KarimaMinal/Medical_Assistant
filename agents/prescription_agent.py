from langchain.prompts import PromptTemplate
from langchain_config import llm

def generate_prescription(diagnosis: str) -> str:
    prompt = PromptTemplate.from_template(
        "Suggest a standard medical prescription for treating: {diagnosis}."
    )
    return llm.predict(prompt.format(diagnosis=diagnosis))
