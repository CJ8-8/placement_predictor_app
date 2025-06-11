import streamlit as st
import pickle
import pandas as pd
import sqlite3

model = pickle.load(open("models/placement_model.pkl", "rb"))

st.title("🎓 Placement Predictor App")

cgpa = st.slider("CGPA", 5.0, 10.0, 7.5)
internships = st.number_input("No. of Internships", 0, 5, 1)
projects = st.number_input("No. of Projects", 0, 10, 2)
comm = st.slider("Communication Skills (1-5)", 1, 5, 3)
cp = st.checkbox("Competitive Programmer?")
dsa = st.slider("DSA Skills (1–5)", 1, 5, 3)
ml = st.checkbox("ML/AI Knowledge?")
cloud = st.checkbox("Cloud Skills?")
backlogs = st.checkbox("Any Backlogs?")
certs = st.number_input("No. of Certifications", 0, 10, 1)
tier = st.selectbox("College Tier", ["Tier 1", "Tier 2", "Tier 3"])
resume = st.slider("Resume Score", 0, 100, 60)

input_data = pd.DataFrame([[cgpa, internships, projects, comm, int(cp), dsa, int(ml),
                            int(cloud), int(backlogs), certs,
                            {"Tier 1": 0, "Tier 2": 1, "Tier 3": 2}[tier], resume]],
                          columns=["CGPA", "Internships", "Projects", "Communication", "CP", "DSA", "ML",
                                   "Cloud", "Backlogs", "Certs", "Tier", "ResumeScore"])

if st.button("Predict Placement Chance"):
    prediction = model.predict(input_data)[0]
    label = {2: "Product-based", 1: "Service-based", 0: "Not Placed"}[prediction]
    st.success(f"You are most likely to be placed in a **{label} company**.")

    conn = sqlite3.connect("database.db")
    input_data["Prediction"] = label
    input_data.to_sql("placements", conn, if_exists="append", index=False)
    conn.close()
