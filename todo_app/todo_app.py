import streamlit as st
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import sqlite3
import os

sqliteConnection = sqlite3.connect("/app/api_development/todo.db")


st.text_area("output",os.getcwd())
st.text_area("output2",sqliteConnection)

cursor = sqliteConnection.cursor()
sqlite_select_query = """CREATE TABLE todo (
	sno INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	"desc" VARCHAR(500) NOT NULL, 
	date_created DATETIME, 
	PRIMARY KEY (sno)
)"""

cursor.execute(sqlite_select_query)
sqliteConnection.commit()

records = cursor.fetchall()

st.text_area("output3",records)

# reading todo table
#df = pd.read_sql(sqlite_select_query,sqliteConnection)
#st.table(df)
