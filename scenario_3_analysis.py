import pandas as pd
from sql_setup import mydb

# Filter Functions
def get_states():
    query = "SELECT DISTINCT States FROM aggregated_transaction"
    df = pd.read_sql(query, mydb)
    return df['States'].sort_values().tolist()

def get_years():
    query = "SELECT DISTINCT Years FROM aggregated_transaction"
    df = pd.read_sql(query, mydb)
    return sorted(df['Years'].tolist())

# Q1: Total transaction amount and count by state for a selected year
def question_1(year):
    query = """
    SELECT States, 
           SUM(Transaction_amount) AS Total_Amount, 
           SUM(Transaction_count) AS Total_Count
    FROM aggregated_transaction
    WHERE Years = %s
    GROUP BY States
    ORDER BY Total_Amount DESC
    """
    return pd.read_sql(query, mydb, params=(year,))

# Q2: Quarterly transaction trends for a selected state and year
def question_2(state, year):
    query = """
    SELECT Quarter, 
           SUM(Transaction_amount) AS Total_Amount, 
           SUM(Transaction_count) AS Total_Count
    FROM aggregated_transaction
    WHERE States = %s AND Years = %s
    GROUP BY Quarter
    ORDER BY Quarter
    """
    return pd.read_sql(query, mydb, params=(state, year))

# Q3: Top 10 states by transaction count in a selected year
def question_3(year):
    query = """
    SELECT States, 
           SUM(Transaction_count) AS Total_Count
    FROM aggregated_transaction
    WHERE Years = %s
    GROUP BY States
    ORDER BY Total_Count DESC
    LIMIT 10
    """
    return pd.read_sql(query, mydb, params=(year,))

# Q4: Payment type-wise transaction distribution for a selected year
def question_4(year):
    query = """
    SELECT Transaction_type, 
           SUM(Transaction_amount) AS Total_Amount
    FROM aggregated_transaction
    WHERE Years = %s
    GROUP BY Transaction_type
    ORDER BY Total_Amount DESC
    """
    return pd.read_sql(query, mydb, params=(year,))

# Q5: Year-on-year growth in transaction amount for a selected state
def question_5(state):
    query = """
    SELECT Years, 
           SUM(Transaction_amount) AS Total_Amount
    FROM aggregated_transaction
    WHERE States = %s
    GROUP BY Years
    ORDER BY Years
    """
    return pd.read_sql(query, mydb, params=(state,))