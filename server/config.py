import os

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('HOST') or 'localhost'
PORT = os.getenv('PORT') or '8080'
