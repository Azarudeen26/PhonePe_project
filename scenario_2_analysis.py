import pandas as pd
from sql_setup import mydb

# Filter Functions
def get_states():
    """Fetch all distinct states from aggregated_user."""
    query = "SELECT DISTINCT States FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return df['States'].sort_values().tolist()

def get_years():
    """Fetch all distinct years from aggregated_user."""
    query = "SELECT DISTINCT Years FROM aggregated_user"
    df = pd.read_sql(query, mydb)
    return sorted(df['Years'].tolist())

def question_1(state, year):
    """
    Q1: Device brand distribution for a given state and year.
    """
    query = """
    SELECT Brands, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE States = %s AND Years = %s
    GROUP BY Brands
    ORDER BY Total_Users DESC
    """
    return pd.read_sql(query, mydb, params=(state, year))

def question_2(state):
    """
    Q2: Yearly device user count trend for a given state.
    """
    query = """
    SELECT Years, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE States = %s
    GROUP BY Years
    ORDER BY Years
    """
    return pd.read_sql(query, mydb, params=(state,))

def question_3(year):
    """
    Q3: Top 10 states by device user count for a given year.
    """
    query = """
    SELECT States, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE Years = %s
    GROUP BY States
    ORDER BY Total_Users DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))

def question_4():
    """
    Q4: Overall brand share across India.
    """
    query = """
    SELECT Brands, SUM(Count) AS Total_Users
    FROM aggregated_user
    GROUP BY Brands
    ORDER BY Total_Users DESC
    """
    return pd.read_sql(query, mydb)

def question_5(year):
    """
    Q5: Top 10 brands by total users for a given year.
    """
    query = """
    SELECT Brands, SUM(Count) AS Total_Users
    FROM aggregated_user
    WHERE Years = %s
    GROUP BY Brands
    ORDER BY Total_Users DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))