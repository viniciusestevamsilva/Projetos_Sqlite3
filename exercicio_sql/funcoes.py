import os
import sqlite3


conn = sqlite3.connect("C:/vinicius/sqlite/exercicio_sql/viagens.db")
conn.execute("PRAGMA foreign_keys = ON;")
cursor = conn.cursor()