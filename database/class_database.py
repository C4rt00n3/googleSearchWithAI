import os
import mysql.connector
from entities import *
from dotenv import load_dotenv

load_dotenv()

class Database:    
    def __init__(self, path_sql: str):
        # Inicia conexão
        self.path_dataset_schema = path_sql
        self.mydb = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("NAME_DATABASE")
        )
        # Cria banco de dados
        self.create_bank()

    def create_bank(self):
        cursor = self.mydb.cursor()

        with open(self.path_dataset_schema, 'r', encoding="utf8") as file:
            queries = file.read()

        for query in queries.split(';'):
            print(query)
            if query.strip():
                cursor.execute(query + ';')
                
    class TopicDatabase:
        # Função para criar um novo tópico
        def __init__(self, mydb) -> None:
            self.mydb = mydb
            
        def create_topic(self, name) -> Topic:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO topic (name) VALUES (%s)"
            val = (name,)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o tópico criado
            cursor.execute("SELECT * FROM topic WHERE id = LAST_INSERT_ID()")
            result = cursor.fetchone()
            return Topic(*result)

        # Função para ler todos os tópicos
        def find_many(self) -> list[Topic]:
            cursor = self.mydb.cursor()
            cursor.execute("SELECT * FROM topic")
            result = cursor.fetchall()
            return [Topic(*row) for row in result]

        # Função para atualizar um tópico
        def update_topic(self, id, name) -> Topic:
            cursor = self.mydb.cursor()
            sql = "UPDATE topic SET name = %s WHERE id = %s"
            val = (name, id)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o tópico atualizado
            cursor.execute("SELECT * FROM topic WHERE id = %s", (id,))
            result = cursor.fetchone()
            return Topic(*result)

        # Função para excluir um tópico
        def delete_topic(self, id):
            cursor = self.mydb.cursor()
            sql = "DELETE FROM topic WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            self.mydb.commit()
            print("Tópico excluído com sucesso")
        
        def find_one(self, id: int) -> Topic | None:
            cursor = self.mydb.cursor()
            sql = "SELECT id, name FROM topic WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                return Topic(*result)
            return None
    
    class ContentDatabase:
        def __init__(self, mydb) -> None:
            self.mydb = mydb
            
        def create_data(self, title, content, link_id) -> Content:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO data (title, content, link_id) VALUES (%s, %s, %s)"
            val = (title, content, link_id)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o dado criado
            cursor.execute("SELECT * FROM data WHERE id = LAST_INSERT_ID()")
            result = cursor.fetchone()
            return Content(*result)

        def update_data(self, id, title, content, link_id) -> Content:
            cursor = self.mydb.cursor()
            sql = "UPDATE data SET title = %s, content = %s, link_id = %s WHERE id = %s"
            val = (title, content, link_id, id)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o dado atualizado
            cursor.execute("SELECT * FROM data WHERE id = %s", (id,))
            result = cursor.fetchone()
            return Content(*result)

        def delete_data(self, id) -> None:
            cursor = self.mydb.cursor()
            sql = "DELETE FROM data WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            self.mydb.commit()
            print("Dado excluído com sucesso")
        
        def find_many(self) -> list[Content]:
            cursor = self.mydb.cursor()
            cursor.execute("SELECT * FROM data")
            result = cursor.fetchall()
            return [Content(*row) for row in result]                

        def find_one(self, id: int) -> Content | None:
            cursor = self.mydb.cursor()
            sql = "SELECT id, title, content, link_id FROM data WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                return Content(*result)
            return None
        
    class LinkDatabase:
        def __init__(self, mydb) -> None:
            self.mydb = mydb
            
        def create_link(self, link, topic_id) -> Link:
            cursor = self.mydb.cursor()
            sql = "INSERT INTO links (link, topic_id) VALUES (%s, %s)"
            val = (link, topic_id)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o link criado
            cursor.execute("SELECT * FROM links WHERE id = LAST_INSERT_ID()")
            result = cursor.fetchone()
            return Link(*result)

        def update_link(self, id, link, topic_id) -> Link:
            cursor = self.mydb.cursor()
            sql = "UPDATE links SET link = %s, topic_id = %s WHERE id = %s"
            val = (link, topic_id, id)
            cursor.execute(sql, val)
            self.mydb.commit()
            
            # Consulta o link atualizado
            cursor.execute("SELECT * FROM links WHERE id = %s", (id,))
            result = cursor.fetchone()
            return Link(*result)

        def delete_link(self, id) -> None:
            cursor = self.mydb.cursor()
            sql = "DELETE FROM links WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            self.mydb.commit()
            print("Link excluído com sucesso")
        
        def find_many(self) -> list[Link]:
            cursor = self.mydb.cursor()
            cursor.execute("SELECT * FROM links")
            result = cursor.fetchall()
            return [Link(*row) for row in result]
        
        def find_one(self, id: int) -> Link | None:
            cursor = self.mydb.cursor()
            sql = "SELECT id, link, topic_id FROM links WHERE id = %s"
            val = (id,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                return Link(*result)
            return None