from sqlalchemy import create_engine, inspect, text
import pytest
from sqlalchemy.sql import text
import time
from sqlalchemy.orm import Session
from CompanyTable import Company
import allure 

db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"

@allure.epic("Компании")
@allure.severity("blocker")
@allure.id("Skypro-1")
@allure.feature("CREATE")
@allure.story("Соединение с базой данных")
@allure.title("Соединение с таблицей company в базе данных")
def test_db_conection():
    with allure.step("Соединение с базой данных"):
        db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    with allure.step("Проверка названия таблицы"):
        assert names[0] == 'company'

@allure.epic("Компании")
@allure.id("Skypro-2")
@allure.feature("CREATE")
@allure.story("Получение списка компаний")
@allure.title("Получение полного списка компаний")
def test_select():
    db = create_engine(db_connection_string)

    with db.connect() as conn:
        statement = text('SELECT * FROM company')
        rows = conn.execute(statement).fetchall()
        rows1 = rows[0]        
        assert rows1[0] == 619
        assert rows1[4] == "FQF_Test"
        assert len(rows) > 0


@allure.epic("Компании")
@allure.severity("blocker")
@allure.id("Skypro-3")
@allure.feature("INSERT")
@allure.story("Создание новой компании")
@allure.title("Создание новой организации")
def test_insert():
    db = create_engine(db_connection_string)
    session = Session(db)
    new_company = Company(name='Test Company_VBA')
    session.add(new_company)
    session.commit()
    return new_company.id
    

@allure.epic("Компании")
@allure.severity("normal")
@allure.id("Skypro-4")
@allure.feature("SELECT")
@allure.story("Получение новой компании по ID")
@allure.title("Получение новой организации по ID")
def test_select_1_row():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        with allure.step("Создание компании в БД"):
            company_id = test_insert()
        with allure.step("Выбираем из списка компанию по id"):
            statement = text('SELECT * FROM company where id = :company_id')
            params = {"company_id": company_id}
            rows = conn.execute(statement, params).fetchall()
        with allure.step("Проверяем что список состоит из одной компании"):
            assert len(rows) == 1
        with allure.step("Проверяем, что название компании совпадает"):
            assert rows[0][4] == 'Test Company_VBA'
            time.sleep(2)
        with allure.step("Удаление компании по id"):
            sql_delete = text("DELETE FROM company WHERE id = :company_id")
            params_delete = {"company_id": company_id}
            conn.execute(sql_delete, params_delete)
            conn.commit()


@allure.epic("Компании")
@allure.severity("critical")
@allure.id("Skypro-5")
@allure.feature("UPDATE")
@allure.story("Изменение данных в поле description")
@allure.title("Изменение данных поля description в новой организации")
@allure.description("Тест создает новую компанию с id = {company_id}, изменяет данные в поле description этой компании, проверяет что поле description приняло изменения, удаляем компанию")
def test_update():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        with allure.step("Создание компании в БД и сохраняем id компании в переменную company_id"):
            company_id = test_insert()
        with allure.step("Изменяем описание компании с id = {company_id}"):
            sql_update = text("UPDATE company SET description = :descr WHERE id = :id")
            params_update = {"descr": 'abracadabra_test', "id": company_id}
            query = conn.execute(sql_update, params_update)
            allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
            conn.commit()
        with allure.step("Считываем описание компании, в которую вносили измнения, по {company_id}"):
            sql_select = text("SELECT description FROM company WHERE id = :id")
            params_select = {"id": company_id}
            result = conn.execute(sql_select, params_select)
            row = result.fetchone()
            updated_description = row[0]
        with allure.step("Проверяем, что описание соответствует внесеным данным"):    
            assert updated_description == "abracadabra_test"
            time.sleep(2)
        with allure.step("Удаляем компанию с  id = {company_id}"):
            sql_delete = text("DELETE FROM company WHERE id = :company_id")
            params_delete = {"company_id": company_id}
            query = conn.execute(sql_delete, params_delete)
            allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
            conn.commit()
        


@allure.epic("Компании")
@allure.severity("blocker")
@allure.id("Skypro-6")
@allure.feature("DELETE")
@allure.story("Удаление компании")
@allure.title("Удаление новой созданной организации по ID")
@allure.description("Тест создает организацию и потом удаляет её из списка по параметру {company_id}")
def test_delete():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        with allure.step("Создание компании в БД и сохраняем id компании в переменную {company_id}"):
            company_id = test_insert()
        with allure.step("Удаляем компанию с  id = {company_id}"):
            sql_delete = text("DELETE FROM company WHERE id = :company_id")
            params_delete = {"company_id": company_id}
            conn.execute(sql_delete, params_delete)
            conn.commit()
        with allure.step("Проверяем, что компания c id = {company_id} больше не существует"):
            sql_select = text("SELECT * FROM company WHERE id = :id")
            params_select = {"id": company_id}
            result = conn.execute(sql_select, params_select)
            assert result.fetchone() is None, "Компания не удалена из базы данных"

   
   