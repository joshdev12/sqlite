import sqlite3
from unittest import result

def create_table(name):
    with sqlite3.connect("oic.db") as conn:
        curs = conn.cursor()

        curs.execute("""
                CREATE TABLE IF NOT EXISTS ? (
                id integer primary key,
                name varchar(50) not null,
                age integer not null,
                email varchar(30) not null unique,
                is_tall bool
                ) 
        """, name)


def insert(name, age, email, is_tall):
    with sqlite3.connect("oic.db") as conn:
        curs = conn.cursor()

    curs.execute("""
            INSERT INTO student (name, age, email, is_tall) VALUES (?, ?, ?, ?)
    """, (name, age, email, is_tall))
    conn.commit()


def get_all():
    with sqlite3.connect("oic.db") as conn:
        curs = conn.cursor()

    data = curs.execute("""
            SELECT * FROM student
    """).fetchall()

    return data

# insert("Kay", 20, "sample@me.com", True)

results = get_all()
print(results)