import random
from EmployeeApi import EmployeeApi
import time
import pytest
from EmployeeApi import Company
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, text



db_connection_string = "postgresql://x_clients_db_r06g_user:0R1RNWXMepS7mrvcKRThRi82GtJ2Ob58@dpg-cj94hf0eba7s73bdki80-a.oregon-postgres.render.com/x_clients_db_r06g"
api = EmployeeApi('https://x-clients-be.onrender.com')


def test_db_conection():
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'company'

def test_insert():
    db = create_engine(db_connection_string)
    session = Session(db)
    new_company = Company(name='Test Company_VBA1')
    session.add(new_company)
    session.commit()
    return new_company.id

def test_db_employee():
    db = create_engine(db_connection_string)
    with db.connect() as conn:
        # Создаем новую компанию
        company_id = test_insert()
        
        # Получаем список сотрудников
        list_query = text('SELECT * FROM employee WHERE company_id = :company_id')
        params = {"company_id": company_id}
        rows = conn.execute(list_query, params).fetchall()
        emp_before = len(rows)
        
        # Добавляем нового сотрудника в компанию
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
        conn.execute(new_employee_query, emp_params)
        rows1 = conn.execute(list_query, params).fetchall()
        emp_after = len(rows1)
        time.sleep(1)
        
        # Находим созданного сотрудника по ID
        emp_id = rows1[-1][0]
        param_id = {"id" : emp_id}
        get_emp_id_query = text("SELECT * FROM employee WHERE id = :id")
        update_id = conn.execute(get_emp_id_query, param_id).fetchone()
        
        # Изменяем данные сотрудника по ID
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
        conn.execute(update_new_employee_query, new_emp_params)
        rows2 = conn.execute(list_query, params).fetchall()
        time.sleep(2)
        
        # Удаляем сотрудника по ID
        delete_id_params = {"id": emp_id}
        delete_query = text('DELETE FROM employee WHERE id = :id')
        conn.execute(delete_query, delete_id_params)
        rows_after_del = conn.execute(list_query, params).fetchall()
        len_after_del = len(rows_after_del)
        time.sleep(1)
        
        # Удаляем компанию
        sql_delete = text("DELETE FROM company WHERE id = :company_id")
        params_delete = {"company_id": company_id}
        conn.execute(sql_delete, params_delete)
        
        assert rows2[-1][8] == new_email
        assert rows2[-1][9] == new_url  
        assert emp_before == 0
        assert emp_before < emp_after
        assert len_after_del < emp_after
        assert rows_after_del == []
        conn.commit()
        # Проверяем, что компания больше не существует
        sql_select = text("SELECT * FROM company WHERE id = :id")
        params_select = {"id": company_id}
        result = conn.execute(sql_select, params_select)
        assert result.fetchone() is None, "Компания не удалена из базы данных"


