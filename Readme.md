#  PhonePe Pulse Data Analysis Dashboard

An **end-to-end data analytics and visualization project** built using **PhonePe Pulse datasets**, **MySQL**, and **Streamlit**.  
This project extracts, stores, analyzes, and visualizes transaction, user, and insurance data to deliver actionable insights on **India’s digital payment trends**.

---

##  Project Overview
The **PhonePe Pulse Data Analysis Dashboard** transforms raw data from PhonePe’s public repository into **meaningful insights** using:
- **Python** for data extraction and analysis
- **MySQL** for structured storage
- **Streamlit** for a fully interactive dashboard

Key capabilities include:
- State-wise, district-wise, and quarterly transaction analysis
- Device usage and user engagement tracking
- Insurance adoption pattern visualization
- GeoJSON-based India map for regional insights
- Scenario-based analysis for strategic decision-making

---

##  Features
- **Five Analytical Scenarios** (5 questions each):
  1. Decoding Transaction Dynamics
  2. Device Dominance & User Engagement
  3. Insurance Penetration & Patterns
  4. Regional Adoption & Performance
  5. User Growth & Engagement Strategy
- **Interactive Filters**:
  - Year, State, District, Quarter
- **Dynamic India Map** (GeoJSON Choropleth)
- **Visualization Types**:
  - Line, Bar, and Pie Charts
  - Data Tables
  - Choropleth Maps

---

##  Dataset
Data sourced from the **PhonePe Pulse GitHub repository**, covering:
- **Aggregated Data**: Transactions, Users, Insurance
- **Map Data**: State/District-level performance
- **Top Data**: Popular categories and brands

---

## Tech Stack
- **Language**: Python
- **Database**: MySQL
- **Libraries**: Pandas, Plotly Express, Streamlit, Requests
- **Mapping**: GeoJSON (India state boundaries)

---
## Project Structure
---bash
PHONEPE_PROJECT/
├── .streamlit/                        # Streamlit configuration (themes, settings)
│   └── config.toml                     # Dark mode and other UI preferences

├── pulse/                              # Raw PhonePe Pulse datasets

├── venv/                               # Python virtual environment (ignored in Git)

├── app.py                              # Main app script or utility functions
├── DB_connection.py                    # MySQL database connection and query helpers
├── streamlit_app.py                    # Main Streamlit dashboard UI
├── scenario_1_analysis.py              # Scenario 1 – Transaction Dynamics Analysis
├── scenario_2_analysis.py              # Scenario 2 – Device Engagement Trends
├── scenario_3_analysis.py              # Scenario 3 – Insurance Penetration Insights
├── scenario_4_analysis.py              # Scenario 4 – Regional & Market Performance
├── scenario_5_analysis.py              # Scenario 5 – User Growth & Engagement
├── sql_setup.py                        # SQL schema creation & data insertion scripts
├── __init__.py                         # Marks directory as a Python package

├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
```
## How to run 

## clone the repository
---bash
git clone https://github.com/your-username/phonepe-data-insights.git
cd phonepe-data-insights
```
## Set up virtual environment
---bash
python -m venv venv
# Windows
venv\Scripts\activate
```

## Install requirement
---bash
pip install -r requirements.txt
```

## Run the streamlit app
---bash
streamlit run streamlit_app.py
```

## Tech stack
---bash
streamlit
pandas
plotly
pymysql
requests
python
```

## Author

* Name: Azarudeen.A
* Qualification: B.Com, MBA
* Experience: 3.5 Years in P2P
* Skills: Python, MySQL, Data Science, Streamlit, Machine Learning, Visualization




