import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

connection = mysql.connector.connect(
            host= os.getenv("MYSQL_HOST"),
            database= os.getenv("MYSQL_DB"),
            user= os.getenv("MYSQL_USER"),
            password='')

mycursor = connection.cursor()

def BitcoinPreco():
    mycursor.execute("CREATE TABLE bitcoin_precos (id int not null, valor int, criptomoeda VARCHAR(32))")