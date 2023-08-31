import random
from EmployeeApi import EmployeeApi
import time
import pytest

api = EmployeeApi('https://x-clients-be.onrender.com')


#1) Получить список сотрудников
@pytest.mark.positive_test
def test_get_all_employee_in_new_company(): 
    result = api.create_company()            #Создаём компанию
    company_id = result['id']                #Записываем в переменную ID компании
    list = api.get_employee_list(company_id) #Получить список сотрудников у компании company_id
    emp_before = len(list)                   #Cохраняем в переменную emp_before размер списка сотрудников
    new_id = ['id']
    #2) Добавить нового сотрудника                              
    firstName = api.generate_random_words(random.randint(1, 1)) 
    lastName = api.generate_random_words(random.randint(1, 1))
    middleName = api.generate_random_words(random.randint(1, 1))
    email = api.generate_random_email()
    companyId = company_id
    url = api.generate_random_url()
    phone = api.generate_random_phone()
    birthdate = api.generate_random_birthdate()
    isActive =  True
    result = api.create_new_employee(new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive) 
    emp_after = result['id']                 #Сохраняем ID нового сотрудника в переменную emp_after
    #Заросить ID нового сотрудника
    new_employee = api.get_employee_id(emp_after)  
    #3)Изменить данные сотрудника
    new_lastName = api.generate_random_words(random.randint(1, 1)) 
    new_email = api.generate_random_email()
    new_url = api.generate_random_url()
    new_phone = api.generate_random_phone()
    isActive =  True
    edited = api.edit_employee(emp_after, new_lastName, new_email, new_url, new_phone, isActive) 
    
    assert edited['email'] == new_email     #Проверить, что изменился email
    assert edited['url'] == new_url         #Проверить, что изменился URL
    assert edited['isActive'] == True       #Проверить, что сотрудник активен
    assert new_employee['id'] == emp_after  #Проверить, что мы получили ID именно нового сотрудника
    assert emp_before == 0                  #Проверить кол-во сотрудников в компании до создания нового.
    assert emp_before < emp_after           #Проверить, что список сотрудников увеличился
    delete = api.delete(company_id)         #Удалить компанию после теста



#1) Получить список сотрудников
@pytest.mark.xfail(strict=True)
@pytest.mark.negative_test
def test_get_all_employee_in_new_company_negative(): 
    result = api.create_company()            #Создаём компанию
    company_id = result['id']                #Записываем в переменную ID компании
    list = api.get_employee_list(company_id) #Получить список сотрудников у компании company_id
    emp_before = len(list)                   #Cохраняем в переменную emp_before размер списка сотрудников
    new_id = ['id']
    #2) Добавить нового сотрудника                              
    firstName = api.generate_random_words(random.randint(1, 1)) 
    lastName = api.generate_random_words(random.randint(1, 1))
    middleName = api.generate_random_words(random.randint(1, 1))
    email = '123@123mail.com'
    companyId = company_id
    url = 'https://storage.yandexcloud.net/yandexpro/storage/images/originals/qZEALznNzzFc0pO7igFzH1qNsrhvp2pOpvNjVzcv.jpg'
    phone = '+79465431321'
    birthdate = '01.01.1990'
    isActive =  True
    result = api.create_new_employee(new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive) 
    emp_after = result['id']                 #Сохраняем ID нового сотрудника в переменную emp_after
    #Заросить ID нового сотрудника
    new_employee = api.get_employee_id(emp_after)  
    #3)Изменить данные сотрудника
    new_lastName = api.generate_random_words(random.randint(1, 1)) 
    #new_email = 'abc@mail.com'
    new_url = ""
    new_phone = '+79465431333'
    isActive =  True
    edited = api.edit_employee(emp_after, new_lastName, new_email, new_url, new_phone, isActive) 
    
    assert edited['email'] == new_email     #Не передаём один из параметров
    assert edited['url'] == new_url         #Проверить, что изменился URL
    assert edited['isActive'] == True       #Проверить, что сотрудник активен
    assert new_employee['id'] == emp_after  #Проверить, что мы получили ID именно нового сотрудника
    assert emp_before == 0                  #Проверить кол-во сотрудников в компании до создания нового.
    assert emp_before == emp_after          #Проверить, что список остался неизменным
    delete = api.delete(company_id)         #Удалить компанию после теста


#Задокументировал изначальный вариант тестов, но они работают только по отдельности, 
#если запускать их разом - идет конфликт и всё падает.

#2) Добавить нового сотрудника 
def test_add_new_employee():
    result = api.create_company()
    company_id = result['id']   
    new_id = ['id']
    firstName = api.generate_random_words(random.randint(1, 1))
    lastName = api.generate_random_words(random.randint(1, 1))
    middleName = api.generate_random_words(random.randint(1, 1))
    email = api.generate_random_email()
    companyId = company_id
    url = api.generate_random_url()
    phone = api.generate_random_phone()
    birthdate = api.generate_random_birthdate()
    isActive =  True
    result = api.create_new_employee(new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = result['id']
    assert emp_id != 0 #Проверить что создался новый пользователь и его ID не равно 0
    time.sleep(1)
    delete = api.delete(company_id)


#3) Получить сотрудника по ID
def test_get_employee_id():
    result = api.create_company()
    company_id = result['id']  
    new_id = ['id']
    firstName = api.generate_random_words(random.randint(1, 1))
    lastName = api.generate_random_words(random.randint(1, 1))
    middleName = api.generate_random_words(random.randint(1, 1))
    email = api.generate_random_email()
    companyId = company_id
    url = api.generate_random_url()
    phone = api.generate_random_phone()
    birthdate = api.generate_random_birthdate()
    isActive =  True
    #result = api.create_new_employee(new_id, companyId, isActive)
    result = api.create_new_employee(new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = result['id']
    new_employee = api.get_employee_id(emp_id)  #Заросить ID нового сотрудника
    assert new_employee['id'] == emp_id         #Проверить что вызванный id сотрудника сотрудника равен созданому новому.
    time.sleep(1)
    delete = api.delete(company_id)
     
#4) Изменить информацию о сотруднике.

def test_edit_employee():  
    result = api.create_company()
    company_id = result['id']  
    new_id = ['id']
    firstName = api.generate_random_words(random.randint(1, 1))
    lastName = api.generate_random_words(random.randint(1, 1))
    middleName = api.generate_random_words(random.randint(1, 1))
    email = api.generate_random_email()
    companyId = company_id
    url = api.generate_random_url()
    phone = api.generate_random_phone()
    birthdate = api.generate_random_birthdate()
    isActive =  True
    result = api.create_new_employee(new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive)
    emp_id = result['id'] 
    new_lastName = api.generate_random_words(random.randint(1, 1))
    new_email = api.generate_random_email()
    new_url = api.generate_random_url()
    new_phone = api.generate_random_phone()
    isActive =  True
    edited = api.edit_employee(emp_id, new_lastName, new_email, new_url, new_phone, isActive)
    assert edited['email'] == new_email
    assert edited['url'] == new_url   
    assert edited['isActive'] == True
    time.sleep(1)
    delete = api.delete(company_id)






