import mysql.connector
import os

class Conexao:

    def __init__(self):
        self.__conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSAWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            port=os.getenv("MYSQL_PORT")
        )

        #  host ='shortline.proxy.rlwy.net',
        #  user = 'root', 
        #  password = 'VSEsRKuGcjkcaggfEsBjgUzVLHqTkjai',
        #  database = 'railway', 
        #  port = 15278
        #  
        #)


    def get_conexao(self):
        return self.__conn
    

    def get_cursor(self):
        return  self.__conn.cursor()
    
    def fechar_conexao(self):
        self.__conn.close()
        self.__conn.cursor().close()


# c = Conexao()
# print(c.get_conexao().is_connected())