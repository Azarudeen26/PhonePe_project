import pandas as pd
from sql_setup import mydb

#Filter functions 
def get_states():
    query = "SELECT DISTINCT States FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return df['States'].sort_values().tolist()

def get_years():
    query = "SELECT DISTINCT Years FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return sorted(df['Years'].tolist())

def get_districts(state, year):
    query = """
    SELECT DISTINCT District FROM map_user
    WHERE States = %s AND Years = %s
    """
    df = pd.read_sql(query, mydb, params=(state, year))
    return df['District'].sort_values().tolist()

# --- Question functions ---
def question_1(state, year):
    # Registrations by Quarter from aggregated_user (Brands combined)
    query = """
    SELECT Quarter, SUM(Count) AS Total_Registrations
    FROM aggregated_user
    WHERE States = %s AND Years = %s
    GROUP BY Quarter
    ORDER BY Quarter
    """
    return pd.read_sql(query, mydb, params=(state, year))

def question_2(state, year):
    # Registrations by District from map_user table (has District column)
    query = """
    SELECT District, SUM(RegisteredUsers) AS Total_Registrations
    FROM map_user
    WHERE States = %s AND Years = %s
    GROUP BY District
    ORDER BY Total_Registrations DESC
    """
    return pd.read_sql(query, mydb, params=(state, year))

def question_3(year):
    # Top 10 States from aggregated_user table
    query = """
    SELECT States, SUM(Count) AS Total_Registrations
    FROM aggregated_user
    WHERE Years = %s
    GROUP BY States
    ORDER BY Total_Registrations DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))

def question_4(state, year):
    # Top 10 Districts by registrations from map_user table
    query = """
    SELECT District, SUM(RegisteredUsers) AS Total_Registrations
    FROM map_user
    WHERE States = %s AND Years = %s
    GROUP BY District
    ORDER BY Total_Registrations DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(state, year))

def question_5(year):
    # Top 10 Pincodes from top_user table (has Pincode column as "Pincode")
    query = """
    SELECT Pincode, SUM(RegisteredUsers) AS Total_Registrations
    FROM top_user
    WHERE Years = %s
    GROUP BY Pincode
    ORDER BY Total_Registrations DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))