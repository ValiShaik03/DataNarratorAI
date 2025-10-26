# 🧠 DataNarratorAI — AI-Powered Data Storyteller

**DataNarratorAI** is an intelligent, interactive Streamlit application that transforms your raw datasets into meaningful insights, visualizations, and AI-driven summaries — all through natural language queries.

It combines the power of **Exploratory Data Analysis (EDA)**, **Visualization**, and **Generative AI (LLMs)** to help users *understand their data like a story.*

---

## 🌐 Live Demo

🚀 **Try it here:** [DataNarratorAI on Streamlit Cloud](https://datanarratorai.streamlit.app)

*(No setup required — includes a built-in sample dataset for instant testing.)*


## ✨ Features

 **Smart Data Upload or Auto Demo Dataset** — Upload your own CSV/Excel file or explore instantly using the built-in Superstore dataset.  
 **Automated EDA** — Get key statistics: missing values, duplicates, numeric/categorical columns, etc.  
 **Interactive Visualizations** — Auto-generates bar, line, and distribution plots for quick understanding.  
 **AI-Powered Insights** — Uses OpenAI to summarize your data and uncover hidden trends.  
 **Chat with Your Data** — Ask natural language questions like *“Which category has the highest profit?”* or *“What’s the correlation between discount and sales?”*  
 **Error Handling** — Automatically handles different file encodings (UTF-8, Latin1).  

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Libraries:** Pandas, Plotly, OpenAI, LangChain  
- **ML/AI:** GPT models for data storytelling  
- **Visualization:** Plotly, Matplotlib, Seaborn    

---

## 📂 Project Structure
```bash
DataNarratorAI/
│
├── app.py # Main Streamlit app
├── data/
│ └── sample_dataset.csv # Ready-to-run default dataset
│
├── utils/
│ ├── data_loader.py # Data loading and cleaning logic
│ ├── eda.py # EDA summary and visualization
│ ├── insight_generator.py # AI-based data insight generator
│ └── chat_module.py # Chat-with-data engine
│
├── requirements.txt # Project dependencies
└── .env # YOUR OPENAI API KEY
```

---

## 🚀 How to Run Locally

1️⃣ **Clone this Repository**
```bash
git clone https://github.com/<your-username>/DataNarratorAI.git
cd DataNarratorAI
```
2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
3️⃣ Set Your OpenAI API Key
```
OPENAI_API_KEY "your_api_key_here"   # Windows
```
4️⃣ Run the App
```
streamlit run app.py
```
🧩 Future Enhancements

 - Add “Suggested Questions” clickable interface

 - Support for multiple datasets

 - PDF/CSV download of AI insights

 - Integration with Power BI for advanced visualization

 - Voice-based query input

🏅 Author

👨‍💻 Shaik Mahaboob Vali

📧 mvali060103@gmail.com

🔗https://linkedin.com/in/mahaboobvalishaik/ 

⭐ If you like this project, consider giving it a star on GitHub! ⭐
