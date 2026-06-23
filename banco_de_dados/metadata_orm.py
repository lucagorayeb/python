from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

engine = create_engine("sqlite+pysqlite:///:memory", echo=True)

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE teste (id INTEGER NOT NULL, nome TEXT NOT NULL);"))
    conn.execute(text("INSERT INTO teste (id, nome) VALUES (:id, :nome)"), 
                    [{"id": 1, "nome": 'Luca'}, {"id": 2, "nome": 'Larissa'}],
                )
    conn.commit() 

with engine.connect() as conn:
    result = conn.execute(text('SELECT * FROM teste;'))
    print(result.all())