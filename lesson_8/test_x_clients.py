import random
from CompanyApi import CompanyApi
import time

api = CompanyApi('https://x-clients-be.onrender.com')



def test_get_companies(): #Получаем список всех компаний
    body = api.get_company_list()
    assert len(body) > 0 #Проверяем что список компаний не пустой

def test_get_active_companies(): #Получаем список всех активных компаний 
    all_companies = api.get_company_list()
    active_companies = api.get_company_list(params_to_add={'active' : 'true'})
    assert len(all_companies) > len(active_companies) #Сравниваем что список всех компаний больше списка активных компаний 

def test_add_new(): #2. Создать новую компанию
    body = api.get_company_list()
    len_before = len(body)
    
    name = api.generate_random_words(random.randint(1, 2))
    descr = api.generate_random_words(random.randint(3, 5))
    result = api.create_company(name, descr)
    new_id = result['id']  
    #3. Получить кол-во компаний после создания
    body = api.get_company_list()
    len_after = len(body)
    #4. Проверить что кол-во увеличилось на +1
    #5. Проверить что ID последней компании равен ID новой созданной компании
    #6. Проверить название последней компании и описание 
    assert len_after - len_before == 1
    assert body[-1]["name"] == name
    assert body[-1]["description"] == descr
    assert body[-1]["id"] == new_id

def test_get_one_company(): #Проверить новую компанию
    name = api.generate_random_words(random.randint(1, 2))
    descr = api.generate_random_words(random.randint(3, 5))
    result = api.create_company(name, descr)
    new_id = result['id']  
    new_company = api.get_company_id(new_id)

    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company['id'] == new_id
    assert new_company['isActive'] == True

def test_edit():  #Изменить данные в новой компании
    name = api.generate_random_words(random.randint(1, 2))
    descr = api.generate_random_words(random.randint(3, 5))
    result = api.create_company(name, descr)
    new_id = result['id']  

    new_name = "Updated"
    new_descr = "Random"
    edited = api.edit(new_id, new_name, new_descr)
    assert edited["name"] == new_name
    assert edited["description"] == new_descr
    assert edited['id'] == new_id
    assert edited['isActive'] == True
    
def test_delete(): #Создать и удалить новую компанию
    name = api.generate_random_words(random.randint(1, 2))
    result = api.create_company(name)
    new_id = result['id']

    delete = api.delete(new_id)
    assert delete["name"] == name
    assert delete["description"] == ""
    assert delete['id'] == new_id
    assert delete['isActive'] == True

    time.sleep(1)
    body = api.get_company_list()
    assert body[-1]['id'] != new_id

def test_deactivate(): #деактивировать новую компанию
    name = api.generate_random_words(random.randint(1, 2))
    result = api.create_company(name)
    new_id = result['id']

    body = api.set_active_state(new_id, False)
    assert body["isActive"] == False

def test_deactivate_and_activate_back(): #Активировать и деактивировать новую компанию
    name = api.generate_random_words(random.randint(1, 2))
    result = api.create_company(name)
    new_id = result['id']
    api.set_active_state(new_id, False)
    body = api.set_active_state(new_id, True)
    assert body["isActive"] == True