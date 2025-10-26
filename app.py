import streamlit as st
import pandas as pd
import os
from utils.data_loader import load_data
from utils.eda import perform_eda, show_visuals
from utils.insight_generator import generate_ai_insights
from utils.chat_module import chat_with_data

st.set_page_config(page_title="DataNarratorAI - AI Data Storyteller", layout="wide")

st.title("🧠 DataNarratorAI — AI-Powered Data Storyteller")
st.write("Upload your dataset or use our sample data to explore AI-driven insights and visualizations.")

# File uploader
uploaded_file = st.file_uploader("📂 Upload CSV or Excel File", type=["csv", "xlsx"])

# If no file uploaded, load sample dataset automatically
if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.success("✅ Your dataset has been uploaded successfully.")
else:
    st.info("ℹ️ No file uploaded — loading sample dataset for demonstration.")
    sample_path = os.path.join("data", "sample_dataset.csv")
    df = pd.read_csv(sample_path)
    st.success("✅ Sample dataset loaded successfully!")

# Display dataset preview
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Perform EDA Summary
st.subheader("🔍 Exploratory Data Analysis Summary")
eda_summary = perform_eda(df)
st.json(eda_summary)

# Automatic Visuals
st.subheader("📈 Visualizations")
show_visuals(df)

# AI Insight Generation
st.subheader("🧠 AI-Generated Insights")
insights = generate_ai_insights(df)
st.markdown(insights)

# Chat Interface
st.subheader("💬 Chat with Your Data")
user_query = st.text_input("Ask a question about your dataset:")
if user_query:
    response = chat_with_data(df, user_query)
    st.success(response)
