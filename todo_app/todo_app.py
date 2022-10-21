import streamlit as st
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import sqlite3
import os

st.text_area("output",os.cmd("ll"))
