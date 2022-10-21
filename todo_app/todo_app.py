import streamlit as st
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app/api_development/todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating a database with below schema
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# app title
st.sidebar.title("ToDo Application")

# inputs
title_input = st.sidebar.text_input("ToDo Title",value="")
desc_input = st.sidebar.text_input("ToDo Description",value="")
submit = st.sidebar.button("SUMBIT")

# add new todo record
if submit:
    if len(title_input) > 0 and len(desc_input) > 0:
        todo = Todo(title=title_input, desc=desc_input)
        db.session.add(todo)
        db.session.commit()

# connecting to sqlite3 db
sqliteConnection = sqlite3.connect("/app/api_development/todo.db")
cursor = sqliteConnection.cursor()
sqlite_select_query = """SELECT * from todo"""

# reading todo table
df = pd.read_sql(sqlite_select_query,sqliteConnection)

# function to update todo
def update_record(title,desc):
    todo.title = title
    todo.desc = desc
    db.session.add(todo)
    db.session.commit()

# function to delete todo
def delete_record(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

tick_box_1,tick_box_2 = st.columns(2)

# table display
with tick_box_1:
    display_table = st.checkbox("All ToDos")
    if display_table and len(df) > 1:
        st.table(df)
    elif display_table and len(df) == 0:
        st.error("No records to display add few !!")
        st.text_area("output2",str(df))


# records update/delete
with tick_box_2:
    search_todo = st.checkbox("SEARCH")
    if search_todo:
        serial_num = st.sidebar.number_input('Provide ToDo Serial Number', min_value=0)
        todo = Todo.query.filter_by(sno=serial_num).first()
        if todo != None:
            update_title = st.text_input("ToDo Title to update", value=todo.title)
            update_desc = st.text_input("ToDo desc to update", value=todo.desc)
            update = st.button("UPDATE")
            if update:
                update_record(update_title,update_desc)
            delete = st.button("DELETE")
            if delete:
                delete_record(serial_num)
        elif todo == None and serial_num > 0:
            st.error("ToDo Record does not exists in the database")
