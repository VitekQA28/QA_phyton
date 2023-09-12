from sqlalchemy import create_engine, inspect, text
import pytest
from sqlalchemy.sql import text
import time
from sqlalchemy.orm import Session
from CompanyTable import Company
import allure 

db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"


@allure.id("Skypro-1")
@allure.story("Соединение с базой данных")
def test_db_conection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'company'

@allure.id("Skypro-2")
@allure.story("Получение списка компаний")
def test_select():
    db = create_engine(db_connection_string)

    with db.connect() as conn:
        statement = text('SELECT * FROM company')
        rows = conn.execute(statement).fetchall()
        rows1 = rows[0]        
        assert rows1[0] == 619
        assert rows1[4] == "FQF_Test"
        assert len(rows) > 0

@allure.id("Skypro-3")
@allure.story("Создание новой компании")
def test_insert():
    db = create_engine(db_connection_string)
    session = Session(db)
    new_company = Company(name='Test Company_VBA')
    session.add(new_company)
    session.commit()
    return new_company.id
    


@allure.id("Skypro-4")
@allure.story("Получение новой компании по ID")
def test_select_1_row():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        company_id = test_insert()
        statement = text('SELECT * FROM company where id = :company_id')
        params = {"company_id": company_id}
        rows = conn.execute(statement, params).fetchall()
        assert len(rows) == 1
        assert rows[0][4] == 'Test Company_VBA'
        time.sleep(2)
        sql_delete = text("DELETE FROM company WHERE id = :company_id")
        params_delete = {"company_id": company_id}
        conn.execute(sql_delete, params_delete)
        conn.commit()


@allure.id("Skypro-5")
@allure.story("Изменение данных в поле description в созданной компании")
def test_update():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        company_id = test_insert()
        sql_update = text("UPDATE company SET description = :descr WHERE id = :id")
        params_update = {"descr": 'abracadabra_test', "id": company_id}
        conn.execute(sql_update, params_update)
        conn.commit()
        sql_select = text("SELECT description FROM company WHERE id = :id")
        params_select = {"id": company_id}
        result = conn.execute(sql_select, params_select)
        row = result.fetchone()
        updated_description = row[0]
        assert updated_description == "abracadabra_test"
        time.sleep(2)
        sql_delete = text("DELETE FROM company WHERE id = :company_id")
        params_delete = {"company_id": company_id}
        conn.execute(sql_delete, params_delete)
        conn.commit()
        #



@allure.id("Skypro-6")
@allure.story("Удаление компании")
def test_delete():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        company_id = test_insert()
        sql_delete = text("DELETE FROM company WHERE id = :company_id")
        params_delete = {"company_id": company_id}
        conn.execute(sql_delete, params_delete)
        conn.commit()
        # Проверяем, что компания больше не существует
        sql_select = text("SELECT * FROM company WHERE id = :id")
        params_select = {"id": company_id}
        result = conn.execute(sql_select, params_select)
        assert result.fetchone() is None, "Компания не удалена из базы данных"

   
   