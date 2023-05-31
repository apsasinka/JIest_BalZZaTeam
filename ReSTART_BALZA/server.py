from flask import Flask, render_template, request, redirect, flash
import sqlite3

class ServerCon():
    # Функции для работы с БД
    def get_connection(self):
        conn = sqlite3.connect('RegistryDB.db')
        return conn


    def execute_query(self, query):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows