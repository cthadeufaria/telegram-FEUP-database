import psycopg2
import os



class Database:

    def __init__(self):
        self.host = "db.fe.up.pt"
        self.port = "5432"
        self.user = os.getenv('db_user')
        self.password = os.getenv('db_password')
        self.database = os.getenv('db_name')


    def connect(self):
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )

        except psycopg2.Error as e:
            print("Error connecting to the database:")
            print(e)
        
        return conn


    def test_database(self):
        try:    
            conn = self.connect()
            cur = conn.cursor()
            message = "Connection to database estabilished successfully"
            print(message)
            cur.close()
            conn.close()
            return True, message
        
        except Exception as e:
            print(e)
            return False, e
        