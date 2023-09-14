import random
from EmployeeApi import EmployeeApi
import time
import pytest
from EmployeeDB import Company
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, text
import allure 


db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"
api = EmployeeApi()


@allure.title("Получение списка компаний")
@allure.description("Соединение с базой данных и получение списка компаний")
@allure.feature("Company list")
@allure.severity("Blocker")
def test_db_conection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'company'


@allure.title("Создание новой компании")
@allure.description("Добавление новой компании и получение его id")
@allure.feature("INSERT")
@allure.severity("Critical")
def test_insert():
    with allure.step("Соединяемся с базой данных"):
        db = create_engine(db_connection_string)
        session = Session(db)
    with allure.step("Создаём компанию с наименованием {name}"):
        new_company = Company(name='Test Company_VBA1')
        session.add(new_company)
        session.commit()
    with allure.step("Получаем id новой компании"):
        return new_company.id


@allure.title("Полный цикл работы с новым сотрудником")
@allure.description("Добавление нового сотрудника в компанию и редактирование его персональных данных")
@allure.feature("EMPLOYEE")
@allure.severity("Critical")
def test_db_employee():
    with allure.step("Соединяемся с базой данных"):
        db = create_engine(db_connection_string)
        with db.connect() as conn:
            with allure.step("Создаем новую компанию"):
                company_id = test_insert()
        
            with allure.step("Получаем список сотрудников"):
                list_query = text('SELECT * FROM employee WHERE company_id = :company_id')
                params = {"company_id": company_id}
                rows = conn.execute(list_query, params).fetchall()
                query = conn.execute(list_query, params)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
                with allure.step("Сохраняем список сотрудников до изменений"):
                    emp_before = len(rows)
        
            with allure.step("Добавляем нового сотрудника в компанию с параметрами {firstName}, {lastName}, {phone}."): 
                firstName = api.generate_random_words(random.randint(1, 1)) 
                lastName = api.generate_random_words(random.randint(1, 1))
                phone = api.generate_random_phone()
                emp_params = {
                "first_name" : firstName,
                "last_name" : lastName,
                "company_id" : company_id,
                "phone" : phone
                }        
                new_employee_query = text("INSERT INTO employee (first_name, last_name, company_id, phone) VALUES (:first_name, :last_name, :company_id, :phone)")
                query = conn.execute(new_employee_query, emp_params)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
                rows1 = conn.execute(list_query, params).fetchall()
            with allure.step("Сохраняем список сотрудников после изменений изменений"):
                emp_after = len(rows1)
                time.sleep(1)
        
            with allure.step("Находим созданного сотрудника по ID"):
                emp_id = rows1[-1][0]
                param_id = {"id" : emp_id}
                get_emp_id_query = text("SELECT * FROM employee WHERE id = :id")
                update_id = conn.execute(get_emp_id_query, param_id).fetchone()
                query = conn.execute(get_emp_id_query, param_id)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
        
            with allure.step("Изменяем данные сотрудника по ID"):
                new_lastName = api.generate_random_words(random.randint(1, 1)) 
                new_email = api.generate_random_email()
                new_url = api.generate_random_url()
                new_phone = api.generate_random_phone()
                new_emp_params = {
                    "last_name" : new_lastName,
                    "email" : new_email,
                    "avatar_url" : new_url,
                    "phone" : new_phone,
                    "id" : update_id[0]
                }        
                update_new_employee_query = text('UPDATE employee SET last_name = :last_name, email = :email, avatar_url = :avatar_url, phone = :phone WHERE id = :id')
                query = conn.execute(update_new_employee_query, new_emp_params)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
                rows2 = conn.execute(list_query, params).fetchall()
                time.sleep(2)
            with allure.step("Удаляем сотрудника по ID"):
                delete_id_params = {"id": emp_id}
                delete_query = text('DELETE FROM employee WHERE id = :id')
                query = conn.execute(delete_query, delete_id_params)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)
                rows_after_del = conn.execute(list_query, params).fetchall()
                len_after_del = len(rows_after_del)
                time.sleep(1)
        
            with allure.step("Удаляем компанию по ID = {company_id}"):
                sql_delete = text("DELETE FROM company WHERE id = :company_id")
                params_delete = {"company_id": company_id}
                query = conn.execute(sql_delete, params_delete)
                allure.attach(str(query.context.cursor.query), "SQL", allure.attachment_type.TEXT)

            with allure.step("Проверяем, что email нового сотрудника соответствует {new_email}"):
                assert rows2[-1][8] == new_email
            with allure.step("Проверяем, что avatar_url нового сотрудника соответствует {new_url}"):
                assert rows2[-1][9] == new_url  
            with allure.step("Проверяем, что список содрудников в новой компании равен 0 "):
                assert emp_before == 0
            with allure.step("Проверяем, что список содрудников в компании стал больше чем 0 после добавления нового сотрудника"):
                assert emp_before < emp_after
            with allure.step("Проверяем, что список содрудников в компании стал меньше, после удаления нового сотрудника"):
                assert len_after_del < emp_after
            with allure.step("Проверяем, что список содрудников пустой"):   
                assert rows_after_del == []
            conn.commit()

            with allure.step("Проверяем, что компания с {company_id} больше не существует"):
                sql_select = text("SELECT * FROM company WHERE id = :id")
                params_select = {"id": company_id}
                result = conn.execute(sql_select, params_select)
                assert result.fetchone() is None, "Компания не удалена из базы данных"


