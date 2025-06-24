# 🩺 Medical Prescription AI Assistant

A simple agentic AI application that analyzes user symptoms and returns a possible diagnosis, prescription, and safety advice using `LangChain`, `Streamlit`, and the `Groq` LLM.

---

## 🧠 Features

- ✅ Symptom analysis using LLM (LLaMA-3 via Groq)
- ✅ Prescription generation for common conditions
- ✅ Safety advice using structured prompts
- ✅ Clean and intuitive UI with Streamlit

---

## 🛠️ Tech Stack

| Tool        | Purpose                         |
|-------------|---------------------------------|
| LangChain   | Agent logic and LLM management  |
| Groq API    | LLM backend using LLaMA 3       |
| Streamlit   | Frontend UI for user interaction |
| Python 3.10+| Programming language            |

---

## 🗂️ Directory Structure 

```bash
.
├── app.py                     # Streamlit frontend
├── langchain_config.py       # Groq model setup
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── agents/
    ├── symptom_agent.py      # Agent to analyze symptoms
    ├── prescription_agent.py # Agent to generate prescriptions
    └── safety_agent.py       # Agent to offer safety advice

```
## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# If you face PowerShell script issues, run this once:
Set-ExecutionPolicy RemoteSigned -Scope Process
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

---
## 🧠 Features

- Symptom analysis with LLM (Groq + LLaMA 3)
- Prescription recommendations
- Health safety advice
- Simple and responsive UI with Streamlit

---

## 📌 Notes

- Works best with Groq’s LLaMA-3 models (`llama3-8b-8192`, etc.)
- This is a demo project and not intended for real medical use

---

## 🧾 License

This project is licensed for educational purposes only.
