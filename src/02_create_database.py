import pandas as pd
import sqlite3

df = pd.read_csv("data/cleaned_insurance.csv")

# Create a connection to the SQLite database 
conn = sqlite3.connect("data/insurance.db")

#Saving the cleaned DataFrame to a new table in the SQLite database called insurance customers
df.to_sql("insurance_customers", conn, if_exists="replace", index=False)

# Close the database connection
conn.close()

print("Data saved to SQLite database successfully at data/insurance.db")