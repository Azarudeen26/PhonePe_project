import streamlit as st
import pandas as pd
import plotly.express as px
import scenario_1_analysis as sc1
import json
import requests
from sql_setup import mydb  #existing DB connection


# PAGE CONFIG
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

# SIDEBAR NAVIGATION & FILTERS
st.sidebar.title("PhonePe Pulse Dashboard")
page = st.sidebar.radio("Go to", ["Home", "About"])

if page == "Home":
    st.title("PhonePe Pulse Project Dashboard")
    # Your existing Home page content here
    st.write("Welcome to the PhonePe Pulse dashboard. Explore transaction, user, and insurance data insights.")
    
elif page == "About":
    st.title("About This Project")
    st.markdown("""
    ### PhonePe Pulse Data Analysis & Visualization

    This project presents an end-to-end data analysis and visualization of PhonePe's transaction, user, and insurance data across India.
    Using official datasets from **PhonePe Pulse**, it explores patterns, trends, and insights at national, state, and district levels.

    **Project Journey:**
    1. **Data Extraction**  Retrieved 9 distinct datasets (aggregated, map, and top categories for transactions, users, and insurance) from the PhonePe Pulse repository.
    2. **Data Processing**  Cleaned and structured raw JSON files into pandas DataFrames, with dynamic schema mapping for automation.
    3. **Database Integration**  Inserted all processed datasets into a **MySQL** database using Python, ensuring efficient querying via `REPLACE INTO`.
    4. **Scenario-Based Analysis**  Designed 5 analytical scenarios, each with 5 business-focused questions to extract meaningful insights.
    5. **Interactive Dashboards**  Built Streamlit-based dashboards with:
       - Dark theme
       - Sidebar filters for Year, State, District, Quarter
       - Tab-based navigation for scenarios and questions
       - Dynamic maps of India with state-wise transaction visualizations
    6. **Visualization Tools**  Used Plotly and GeoJSON to create heatmaps, bar charts, and trend lines.

    **Key Insights:**
    - Transaction volume and value patterns across years, quarters, and states
    - Device brand dominance and user growth trends
    - Insurance adoption patterns and penetration rates

    **Technology Stack:**
    - **Languages**: Python (Pandas, Plotly, Streamlit)
    - **Database**: MySQL
    - **Visualization**: Plotly Express, GeoJSON maps
    - **Data Source**: PhonePe Pulse datasets

    **Developer:** [Azarudeen.A]
    """)

st.sidebar.markdown("## Filter Options")
year_list = sc1.get_years()
state_list = sc1.get_states()

selected_year = st.sidebar.selectbox("Year", year_list)
selected_state = st.sidebar.selectbox("State", state_list)

# Example static district list; replace with DB fetch if available
district_list = ["trichy", "chennai", "karnataka"]
selected_district = st.sidebar.selectbox("District", district_list)

quarter_list = [1, 2, 3, 4]
selected_quarter = st.sidebar.selectbox("Quarter", quarter_list)

# TOP-LEVEL TABS FOR SCENARIOS
scenario_tabs = st.tabs([
    "Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", "Scenario 5", "Interactive Map"
])

## SCENARIO 1 Decoding Transaction Dynamics
import scenario_1_analysis as sc1
with scenario_tabs[0]:
    st.markdown("## Scenario 1: Decoding Transaction Dynamics")

    tabs = st.tabs([
        "Q1: State-Quarter Amount",
        "Q2: State-Year Amount",
        "Q3: Top 10 States (by Amount)",
        "Q4: Transaction Type Share",
        "Q5: Top 10 States (by Count)"
    ])

    # Q1
    with tabs[0]:
        df = sc1.question_1(selected_state, selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"{selected_state.title()} - Transaction Amount in {selected_year}")
            fig = px.line(df, x="Quarter", y="Total_Amount", markers=True)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q2
    with tabs[1]:
        df = sc1.question_2(selected_state)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"{selected_state.title()} - Yearly Transaction Amount")
            fig = px.bar(df, x="Years", y="Total_Amount", color="Years")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q3
    with tabs[2]:
        df = sc1.question_3(selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Top 10 States by Transaction Amount in {selected_year}")
            fig = px.bar(df, x="States", y="Total_Amount", color="States")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q4
    with tabs[3]:
        df = sc1.question_4()
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader("Transaction Type Share Across India")
            fig = px.pie(df, names="Transaction_type", values="Total", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q5
    with tabs[4]:
        df = sc1.question_5(selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Top 10 States by Transaction Count in {selected_year}")
            fig = px.bar(df, x="States", y="Total_Count", color="States")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

# # SCENARIO 2 Device Brand Distribution
import scenario_2_analysis as sc2

with scenario_tabs[1]:
    st.markdown("## Scenario 2: Device Brand Distribution")

    tabs = st.tabs([
        "Q1: Brand Share (State-Year)",
        "Q2: Brand Trend (State)",
        "Q3: Top 10 States by Users",
        "Q4: Overall Brand Share",
        "Q5: Top 10 Brands (Year)"
    ])

    # Q1
    with tabs[0]:
        df = sc2.question_1(selected_state, selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Device Brand Share in {selected_state.title()} ({selected_year})")
            fig = px.pie(df, names="Brands", values="Total_Users", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q2
    with tabs[1]:
        df = sc2.question_2(selected_state)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Device Brand Trend in {selected_state.title()} Over the Years")
            fig = px.bar(df, x="Years", y="Total_Users", color="Years")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q3
    with tabs[2]:
        df = sc2.question_3(selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Top 10 States by Device Users in {selected_year}")
            fig = px.bar(df, x="States", y="Total_Users", color="States")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q4
    with tabs[3]:
        df = sc2.question_4()
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader("Overall Device Brand Share Across India")
            fig = px.pie(df, names="Brands", values="Total_Users", hole=0.4)
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

    # Q5
    with tabs[4]:
        df = sc2.question_5(selected_year)
        if df.empty:
            st.warning("No data found for the selected filters.")
        else:
            st.subheader(f"Top 10 Brands by Users in {selected_year}")
            fig = px.bar(df, x="Brands", y="Total_Users", color="Brands")
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(df)

## scenario 3 ( original Scenario 4: Transaction Analysis for Market Expansion)
import scenario_3_analysis as sc3

with scenario_tabs[2]:  
    st.markdown("## Scenario 3: Transaction Analysis for Market Expansion")

    tabs = st.tabs([
        "Q1: State Transaction Amount & Count",
        "Q2: Quarterly Trends (State-Year)",
        "Q3: Top 10 States by Transaction Count",
        "Q4: Payment Type Distribution",
        "Q5: Year-on-Year Growth (State)"
    ])

    # Q1
    with tabs[0]:
        df = sc3.question_1(selected_year)
        if df.empty:
            st.warning("No data found for selected year.")
        else:
            st.subheader(f"Transaction Amount and Count by State in {selected_year}")
            st.dataframe(df)
            fig = px.bar(df, x='States', y=['Total_Amount', 'Total_Count'], barmode='group',
                         labels={'value': 'Amount / Count', 'States': 'State'})
            st.plotly_chart(fig, use_container_width=True, key="sc3_q1")

    # Q2
    with tabs[1]:
        df = sc3.question_2(selected_state, selected_year)
        if df.empty:
            st.warning("No data found for selected filters.")
        else:
            st.subheader(f"Quarterly Transaction Trends in {selected_state} for {selected_year}")
            fig = px.line(df, x='Quarter', y=['Total_Amount', 'Total_Count'], markers=True,
                          labels={'value': 'Amount / Count', 'Quarter': 'Quarter'})
            st.plotly_chart(fig, use_container_width=True, key="sc3_q2")
            st.dataframe(df)

    # Q3
    with tabs[2]:
        df = sc3.question_3(selected_year)
        if df.empty:
            st.warning("No data found for selected year.")
        else:
            st.subheader(f"Top 10 States by Transaction Count in {selected_year}")
            fig = px.bar(df, x='States', y='Total_Count', color='States')
            st.plotly_chart(fig, use_container_width=True, key="sc3_q3")
            st.dataframe(df)

    # Q4
    with tabs[3]:
        df = sc3.question_4(selected_year)
        if df.empty:
            st.warning("No data found for selected year.")
        else:
            st.subheader(f"Payment Type Distribution in {selected_year}")
            fig = px.pie(df, names='Transaction_type', values='Total_Amount', hole=0.4)
            st.plotly_chart(fig, use_container_width=True, key="sc3_q4")
            st.dataframe(df)

    # Q5
    with tabs[4]:
        df = sc3.question_5(selected_state)
        if df.empty:
            st.warning("No data found for selected state.")
        else:
            st.subheader(f"Year-on-Year Transaction Amount Growth in {selected_state}")
            fig = px.bar(df, x='Years', y='Total_Amount', color='Years')
            st.plotly_chart(fig, use_container_width=True, key="sc3_q5")
            st.dataframe(df)

### # Scenario 4 Tab (original Scenario 5: User Engagement and Growth Strategy)
import scenario_4_analysis as sc4

with scenario_tabs[3]:
    st.markdown("## Scenario 4: User Engagement and Growth Strategy")

    tabs = st.tabs([
        "Q1: Quarterly Users",
        "Q2: Yearly Users Trend",
        "Q3: Top 10 States by Users"
    ])

    # Q1
    with tabs[0]:
        df = sc4.question_1(selected_state, selected_year)
        if df.empty:
            st.warning("No data found for selected filters.")
        else:
            st.subheader(f"Quarterly User Count in {selected_state} ({selected_year})")
            fig = px.bar(df, x="Quarter", y="Total_Users", color="Quarter")
            st.plotly_chart(fig, use_container_width=True, key="sc4_q1")
            st.dataframe(df)

    # Q2
    with tabs[1]:
        df = sc4.question_2(selected_state)
        if df.empty:
            st.warning("No data found for selected filters.")
        else:
            st.subheader(f"Yearly User Trend in {selected_state}")
            fig = px.line(df, x="Years", y="Total_Users", markers=True)
            st.plotly_chart(fig, use_container_width=True, key="sc4_q2")
            st.dataframe(df)

    # Q3
    with tabs[2]:
        df = sc4.question_3(selected_year)
        if df.empty:
            st.warning("No data found for selected filters.")
        else:
            st.subheader(f"Top 10 States by Users in {selected_year}")
            fig = px.bar(df, x="States", y="Total_Users", color="States")
            st.plotly_chart(fig, use_container_width=True, key="sc4_q3")
            st.dataframe(df)

 ## scenario 5  (original Scenario 8: User Registration Analysis)
import scenario_5_analysis as sc5

with scenario_tabs[4]:
    st.markdown("## Scenario 5: User Registration Analysis")
    tabs = st.tabs([
        "Q1: Registrations by Quarter",
        "Q2: Registrations by District",
        "Q3: Top 10 States",
        "Q4: Top 10 Districts",
        "Q5: Top 10 Pincodes"
    ])

with tabs[0]:
    st.subheader("Q1: Total User Registrations by Quarter")
    df = sc5.question_1(selected_state, selected_year)
    fig = px.bar(df, x='Quarter', y='Total_Registrations',
                 title=f"Registrations by Quarter in {selected_state} ({selected_year})")
    st.plotly_chart(fig, use_container_width=True, key="sc5_q1")

with tabs[1]:
    st.subheader("Q2: Total User Registrations by District")
    df = sc5.question_2(selected_state, selected_year)
    fig = px.bar(df, x='District', y='Total_Registrations',
                 title=f"Registrations by District in {selected_state} ({selected_year})")
    st.plotly_chart(fig, use_container_width=True, key="sc5_q2")

with tabs[2]:
    st.subheader("Q3: Top 10 States by Registrations")
    df = sc5.question_3(selected_year)
    fig = px.bar(df, x='States', y='Total_Registrations',
                 title=f"Top 10 States by Registrations in {selected_year}")
    st.plotly_chart(fig, use_container_width=True, key="sc5_q3")

with tabs[3]:
    st.subheader("Q4: Top 10 Districts by Registrations")
    df = sc5.question_4(selected_state, selected_year)
    fig = px.bar(df, x='District', y='Total_Registrations',
                 title=f"Top 10 Districts by Registrations in {selected_state} ({selected_year})")
    st.plotly_chart(fig, use_container_width=True, key="sc5_q4")

with tabs[4]:
    st.subheader("Q5: Top 10 Pincodes by Registrations")
    df = sc5.question_5(selected_year)
    fig = px.bar(df, x='Pincode', y='Total_Registrations',
                 title=f"Top 10 Pincodes by Registrations in {selected_year}")
    st.plotly_chart(fig, use_container_width=True, key="sc5_q5")
  
## Map interactive 
with scenario_tabs[5]:
    st.header("Interactive Transaction Map of India")

    @st.cache_data
    def get_map_data(year):
        query = f"""
        SELECT States, SUM(Transaction_amount) AS Total_Amount 
        FROM aggregated_transaction 
        WHERE Years = {year} 
        GROUP BY States
        """
        return pd.read_sql(query, mydb)

    # Fetch transaction data
    df_map = get_map_data(selected_year)

    # --- Load India States GeoJSON ---
    geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response = requests.get(geojson_url)
    india_states = json.loads(response.text)

    # --- Inspect State Names in GeoJSON ---
    # geo_states = [feature["properties"]["ST_NM"] for feature in india_states["features"]]
    # st.write("States in GeoJSON:", geo_states)

    # --- Map your DB state names to match GeoJSON state names ---
    state_name_map = {
        "andaman-&-nicobar-islands": "Andaman & Nicobar Islands",
        "andhra-pradesh": "Andhra Pradesh",
        "arunachal-pradesh": "Arunachal Pradesh",
        "assam": "Assam",
        "bihar": "Bihar",
        "chhattisgarh": "Chhattisgarh",
        "goa": "Goa",
        "gujarat": "Gujarat",
        "haryana": "Haryana",
        "himachal-pradesh": "Himachal Pradesh",
        "jammu-&-kashmir": "Jammu & Kashmir",
        "jharkhand": "Jharkhand",
        "karnataka": "Karnataka",
        "kerala": "Kerala",
        "madhya-pradesh": "Madhya Pradesh",
        "maharashtra": "Maharashtra",
        "manipur": "Manipur",
        "meghalaya": "Meghalaya",
        "mizoram": "Mizoram",
        "nagaland": "Nagaland",
        "odisha": "Odisha",
        "punjab": "Punjab",
        "rajasthan": "Rajasthan",
        "sikkim": "Sikkim",
        "tamil-nadu": "Tamil Nadu",
        "telangana": "Telangana",
        "tripura": "Tripura",
        "uttar-pradesh": "Uttar Pradesh",
        "uttarakhand": "Uttarakhand",
        "west-bengal": "West Bengal",
        "nct-of-delhi": "NCT of Delhi",
        "ladakh": "Ladakh",
        "puducherry": "Puducherry",
        "chandigarh": "Chandigarh",
        "daman-&-diu": "Daman & Diu",
        "dadra-&-nagar-haveli": "Dadra & Nagar Haveli"
    }

    # Convert state names to match GeoJSON
    df_map["States"] = df_map["States"].str.lower().map(state_name_map)

    # --- Plot the Choropleth Map ---
    if not df_map.empty:
        fig = px.choropleth(
            df_map,
            geojson=india_states,
            featureidkey="properties.ST_NM",
            locations="States",
            color="Total_Amount",
            color_continuous_scale="Viridis",
            range_color=(df_map["Total_Amount"].min(), df_map["Total_Amount"].max()),
            hover_name="States",
            hover_data={"Total_Amount": True},
            title=f"Total PhonePe Transactions in {selected_year}",
        )

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(
            margin={"r": 0, "t": 50, "l": 0, "b": 0},
            coloraxis_colorbar=dict(title="Total Amount"),
        )

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(df_map)
    else:
        st.warning(f"No transaction data found for the year {selected_year}.")