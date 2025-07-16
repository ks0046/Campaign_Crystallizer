# Campaign Crystallizer

A Streamlit web app that analyzes local Reddit discourse (e.g., from r/pittsburgh) to identify the most discussed civic issues and generate AI-assisted policy platform planks.
---

## 🔍 Features

- 📊 **Visualize Most Discussed Local Issues** using bar charts  
- ☁️ **Generate Word Cloud** from Reddit post content  
- 🧠 **AI-Powered Platform Plank Generator** using OpenAI API  
- 🔍 **Drill Down by Issue Category** with detailed Reddit post listings  
- 🧱 **View Suggested Platform Planks** per issue category  
---

## 🚀 Live App

Link to the App: https://pittsburghcampaigncrystallizer.streamlit.app/
---

## 🗂️ Project Structure

campaign_crystallizer/
├── data/
│ ├── cleaned_posts.csv
│ └── platform_planks.csv
├── scripts/
│ ├── clean_and_label.py
│ ├── platform_plank_generator.py
│ └── visualise.py
├── .streamlit/
│ └── secrets.toml (excluded from Git)
├── requirements.txt
└── README.md
---

## 🛠️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/ks0046/Campaign_Crystallizer.git
   cd Campaign_Crystallizer

2. Install Required Dependencies
pip install -r requirements.txt

3. Add your OpenAI API key
Create a .streamlit/secrets.toml file and paste:
OPENAI_API_KEY = "your-api-key-here"

4. Launch the app
streamlit run scripts/visualise.py

🧩 Tech Stack
Streamlit
Pandas
Plotly
WordCloud
OpenAI API

👩‍💻 Author
Kriti Samnotra
🎓 Carnegie Mellon University — Master of Science in Public Policy and Management, D.C. Track
🔗 https://www.linkedin.com/in/kriti-samnotra/

