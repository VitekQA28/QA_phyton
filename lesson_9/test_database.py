from sqlalchemy import create_engine, inspect, text
import pytest
from sqlalchemy.sql import text
import time

db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"

def test_db_conection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'company'


def test_select():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        statement = text('SELECT * FROM company')
        rows = conn.execute(statement).fetchall()
        rows1 = rows[0]
        
        assert rows1[0] == 619
        assert rows1[4] == "FQF_Test"
        assert len(rows) > 0

def test_select_1_row():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        statement = text('SELECT * FROM company where id = :company_id')
        params = {
            "company_id": 1419,
            "isActive" : True
            }
        rows = conn.execute(statement, params).fetchall()
    assert len(rows) == 1
    assert rows[0][4] == 'QA Auto'


def test_insert():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        name_company = {"new_name" : 'Test Company_VB'}
        sql = text("insert into company(\"name\") values (:new_name)")
        add_new = conn.execute(sql, name_company)
        time.sleep(2)
        select_sql = text("SELECT * FROM company WHERE \"name\" = :new_name")
        rows = conn.execute(select_sql, name_company).fetchall()
        print(rows[0][0])
        assert len(rows) >= 1
        assert rows[0][4] == 'Test Company_VB'

def test_update():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        sql = text("UPDATE company SET description = :descr WHERE id = :id")
        params = {"descr": 'abracadabra', "id": 1419}
        rows = conn.execute(sql, params)
        
        

    