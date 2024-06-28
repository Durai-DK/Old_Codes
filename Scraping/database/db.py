import sqlite3
import pandas as pd

df = pd.read_excel(r'C:\Users\admin\Downloads\Laptop Price Lists 14-06-2023.xlsx', sheet_name='Sheet1')
conn = sqlite3.connect('sqlite.db')

df.to_sql('your_table', conn, if_exists='replace', index=False)

conn.close()
