import os
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host = os.getenv("HOST"),
        user = os.getenv("USER"),
        password = os.getenv("PASS"),
        port = os.getenv("PORT"),
        db = os.getenv("DB")
    )