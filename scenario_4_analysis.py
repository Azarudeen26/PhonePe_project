import pandas as pd
from sql_setup import mydb

# Filter functions
def get_states():
    query = "SELECT DISTINCT States FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return sorted(df['States'].tolist())

def get_years():
    query = "SELECT DISTINCT Years FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return sorted(df['Years'].tolist())

def get_districts(state, year):
    # Try with District column, fallback to empty list if error
    try:
        query = """
        SELECT DISTINCT District
        FROM aggregated_user
        WHERE States = %s AND Years = %s
        """
        df = pd.read_sql(query, mydb, params=(state, year))
        return sorted(df['District'].tolist())
    except Exception:
        return []

# Question 1: Quarterly user and app opens
def question_1(state, year):
    query = """
    SELECT Quarter, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE States = %s AND Years = %s
    GROUP BY Quarter
    ORDER BY Quarter
    """
    return pd.read_sql(query, mydb, params=(state, year))

# Question 2: Yearly user and app opens trend
def question_2(state):
    query = """
    SELECT Years, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE States = %s
    GROUP BY Years
    ORDER BY Years
    """
    return pd.read_sql(query, mydb, params=(state,))

# Question 3: Top 10 states by users
def question_3(year):
    query = """
    SELECT States, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE Years = %s
    GROUP BY States
    ORDER BY Total_Users DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))

