import sqlite3 as sql

def createDB():
    conn = sql.connect("libreria.db")
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE ordenes_de_compra (
                id INTEGER PRIMARY KEY,
                libro TEXT NOT NULL,
                direccion_envio TEXT NOT NULL,
                telefono TEXT NOT NULL
        
        )"""

    )
    conn.commit()
    conn.close()

def createTable():
    conn = sql.connect("libreria.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE usuarios (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
        
        )"""

    )
    conn.commit()
    conn.close()    


if __name__ == "__main__":
    createTable()
    