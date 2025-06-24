import streamlit as st
from agents.symptom_agent import analyze_symptoms
from agents.prescription_agent import generate_prescription
from agents.safety_agent import get_safety_advice

st.set_page_config(page_title="Medical Assistant", page_icon="🩺")
st.title("🩺 AI Medical Prescription Assistant")

symptoms = st.text_area("Enter symptoms (comma-separated):")

if st.button("Get Diagnosis & Advice"):
    if not symptoms.strip():
        st.warning("Please enter symptoms.")
    else:
        with st.spinner("Analyzing symptoms..."):
            diagnosis = analyze_symptoms(symptoms)
            prescription = generate_prescription(diagnosis)
            advice = get_safety_advice(diagnosis)

        st.subheader("Diagnosis")
        st.write(diagnosis)

        st.subheader("Prescription")
        st.write(prescription)

        st.subheader("Safety Advice")
        st.write(advice)
