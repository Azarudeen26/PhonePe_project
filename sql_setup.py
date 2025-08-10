import pymysql
from DB_connection import Agg_insurance,Agg_Trans,Agg_user,map_insurance,map_trans,map_user,top_insurance,top_Trans,top_user  # ✅ Importing your DataFrame

# Create a database connection
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="phonepe",
    #cursorclass=pymysql.cursors.DictCursor
)
cursor = mydb.cursor()

# Create table with PRIMARY KEY to define uniqueness
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aggregated_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Insurance_type VARCHAR(50),
        Insurance_count BIGINT,
        Insurance_amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, Insurance_type)
    )
''')
mydb.commit()

# Insert or update rows (avoids duplicates)
for index, row in Agg_insurance.iterrows():
    replace_query = '''
        REPLACE INTO aggregated_insurance (
            States, Years, Quarter, Insurance_type, Insurance_count, Insurance_amount
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))

mydb.commit()

print(f" Successfully inserted or updated {len(Agg_insurance)} rows into aggregated_insurance")

# Create table for aggregated transactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aggregated_transaction (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Transaction_type VARCHAR(50),
        Transaction_count BIGINT,
        Transaction_amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, Transaction_type)
    )
''')
mydb.commit()

# Insert or update rows (REPLACE INTO avoids duplicates)
for index, row in Agg_Trans.iterrows():
    replace_query = '''
        REPLACE INTO aggregated_transaction (
            States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))

mydb.commit()

print(f" Successfully inserted or updated {len(Agg_Trans)} rows into aggregated_transaction")

#Create and Insert: Aggregated User ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS aggregated_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Brands VARCHAR(50),
        Count BIGINT,
        Percentage FLOAT,
        PRIMARY KEY (States, Years, Quarter, Brands)
    )
''')
mydb.commit()

# Insert or update rows (REPLACE INTO avoids duplicates)
for index, row in Agg_user.iterrows():
    replace_query = '''
        REPLACE INTO aggregated_user (
            States, Years, Quarter, Brands, Count, Percentage
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))
mydb.commit()
print(f" Successfully inserted or updated {len(Agg_user)} rows into aggregated_user")

# Create and Insert: Map Insurance ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS map_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(100),
        Count BIGINT,
        Amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, District)
    )
''')
mydb.commit()
# Insert or update rows (REPLACE INTO avoids duplicates)
for index, row in map_insurance.iterrows():
    replace_query = '''
        REPLACE INTO map_insurance (
            States, Years, Quarter, District, Count, Amount
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))
mydb.commit()
print(f" Successfully inserted or updated {len(map_insurance)} rows into map_insurance")

# # # --- Create and Insert: Map Transaction ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS map_transaction (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(100),
        Count BIGINT,
        Amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, District)
    )
''')
mydb.commit()
# Insert or update rows (REPLACE INTO avoids duplicates)
for index, row in map_trans.iterrows():
    replace_query = '''
        REPLACE INTO map_transaction (
            States, Years, Quarter, District, Count, Amount
        ) VALUES (%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))
mydb.commit()
print(f" Successfully inserted or updated {len(map_trans)} rows into map_transaction")

# # Create and Insert: Map User ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS map_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        District VARCHAR(100),
        RegisteredUsers BIGINT,
        AppOpens BIGINT,
        PRIMARY KEY (States, Years, Quarter, District)
    )
''')
mydb.commit()

# # Insert Using REPLACE INTO ---
replace_query = '''
    REPLACE INTO map_user (
        States, Years, Quarter, District, RegisteredUsers, AppOpens
    ) VALUES (%s, %s, %s, %s, %s, %s)
'''

for index, row in map_user.iterrows():
    cursor.execute(replace_query, (
        row['States'],
        row['Years'],
        row['Quarter'],
        row['District'],
        row['RegisteredUsers'],
        row['AppOpens']
    ))

mydb.commit()

print(f" Successfully inserted or updated {len(map_user)} rows into map_user")

# Create and Insert: Top Insurance ---
create_query = '''
    CREATE TABLE IF NOT EXISTS top_insurance (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincode INT,
        count BIGINT,
        Amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, Pincode)
    )
'''
cursor.execute(create_query)
mydb.commit()

# --- Insert Data ---
insert_query = '''
    REPLACE INTO top_insurance (
        States, Years, Quarter, Pincode, count, Amount
    ) VALUES (%s, %s, %s, %s, %s, %s)
'''

for index, row in top_insurance.iterrows():
    cursor.execute(insert_query, tuple(row.values))

mydb.commit()
print(f" Successfully inserted or updated {len(top_insurance)} rows into top_insurance.")

# #Create and Insert: Top_transcation
create_query = '''
    CREATE TABLE IF NOT EXISTS top_transaction (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincode INT,
        Count BIGINT,
        Amount BIGINT,
        PRIMARY KEY (States, Years, Quarter, Pincode)
    )
'''
cursor.execute(create_query)
mydb.commit()

# #Insert or update rows (REPLACE INTO avoids duplicates)
insert_query = '''
    REPLACE INTO top_transaction (
        States, Years, Quarter, Pincode, Count, Amount
    ) VALUES (%s, %s, %s, %s, %s, %s)
'''

for index, row in top_Trans.iterrows():
    cursor.execute(insert_query, tuple(row.values))

mydb.commit()
print(f" Successfully inserted or updated {len(top_Trans)} rows into top_transaction.")

# #Create and Insert: Top User ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS top_user (
        States VARCHAR(50),
        Years INT,
        Quarter INT,
        Pincode INT,
        RegisteredUsers BIGINT,
        PRIMARY KEY (States, Years, Quarter, Pincode)
    )
''')
mydb.commit()
# Insert or update rows (REPLACE INTO avoids duplicates)
for index, row in top_user.iterrows():
    replace_query = '''
        REPLACE INTO top_user (
            States, Years, Quarter, Pincode, RegisteredUsers
        ) VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(replace_query, tuple(row))
mydb.commit()
print(f" Successfully inserted or updated {len(top_user)} rows into top_user")

# # Close connection
# cursor.close()
# mydb.close()