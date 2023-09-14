import requests
import random
from faker import Faker
import string
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import allure 

@allure.suite("Работа с данными через API")
class EmployeeApi:
  
    @allure.title("Генерация рандомного текста {num_words}")
    def generate_random_words(self, num_words: int)->str:  
        """
        Эта функция генерирует рандомный текст 
        """
        fake = Faker()
        words = [fake.word() for _ in range(num_words)]
        return ' '.join(words)
    

    @allure.title("Генерация рандомного email")
    def generate_random_email(self)->str:
        """
        Эта функция генерирует рандомный email 
        """
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{random_string}@example.com"
        return email
    
    @allure.title("Генерация рандомного номера телефона")
    def generate_random_phone(self)->str:
        """
        Эта функция генерирует рандомный номер телефона 
        """
        phone = '+7' + ''.join(random.choices(string.digits, k=10))
        return phone
    
    @allure.title("Генерация рандомного URL")
    def generate_random_url(self)->str:
        """
        Эта функция генерирует рандомный URL
        """
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        url = f"https://example.com/{random_string}"
        return url


'''
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class CompanyTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):        
        with self.db.connect() as conn:
            statement = text('SELECT * FROM company')
            return conn.execute(statement).fetchall()
'''   

'''
      @allure.title("Получение новой организации по ID")
    def __init__(self, url)->None:
        self.url = url

    @allure.title("Получение новой организации по ID")
    def get_company_list(self, params_to_add = None)->list:
        resp = requests.get(self.url +'/company', params= params_to_add) 
        return resp.json()
    
    @allure.title("Получение новой организации по ID")
    def get_token(self, user = 'leonardo', password = 'leads' )->str:    
        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds) 
        return resp.json()["userToken"]
        
    def create_company(self, name = None, description = None):
        if name is None:
            name = self.generate_random_words(random.randint(1, 2))
        if description is None:
            description = self.generate_random_words(random.randint(2, 2))

        company = {
            'name': name,
            'description': description
         }
        my_headers ={}
        my_headers['x-client-token'] = self.get_token() 
        resp = requests.post(self.url+'/company', json=company, headers=my_headers)

        
        return resp.json()

    def get_company_id(self, id):
        resp = requests.get(self.url +'/company/'+str(id))
        return resp.json() 
    
    def get_employee_list(self, company_id):
        resp = requests.get(self.url + '/employee', params={'company': company_id})
        return resp.json()
    
    def get_employee_id(self, id):
        resp = requests.get(self.url +'/employee/'+str(id))
        return resp.json() 
    
    def edit_employee(self, new_id, lastName, email, url, phone, isActive):
        my_headers ={}
        my_headers['x-client-token'] = self.get_token()
        employee = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": True
        }
        resp = requests.patch(self.url +'/employee/'+str(new_id), headers=my_headers, json=employee)
        return resp.json()   
     
    

    def create_new_employee(self, isActive, new_id, companyId, firstName =None, lastName=None, middleName=None, email=None, url=None, phone=None, birthdate=None):
        if firstName is None:
            firstName = self.generate_random_words(random.randint(1, 1))
        if lastName is None:
            lastName = self.generate_random_words(random.randint(1, 1))
        if middleName is None:
            middleName = self.generate_random_words(random.randint(1, 1))
        if email is None:
            email = self.generate_random_email()
        if url is None:
            url = self.generate_random_url()
        if phone is None:
            phone = self.generate_random_phone()
        if birthdate is None:
            birthdate = self.generate_random_birthdate()
           
    
    def create_new_employee(self, new_id, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):  
        employee = {
            "id": new_id,
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": True
        }
        my_headers ={}
        my_headers['x-client-token'] = self.get_token() 
        resp = requests.post(self.url+'/employee', json=employee, headers=my_headers)
        return resp.json()
        
        
        def delete(self, id):
        my_headers ={}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.get(self.url +'/company/delete/'+str(id), headers=my_headers)
        return resp.json()
        '''

'''
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class CompanyTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):        
        with self.db.connect() as conn:
            statement = text('SELECT * FROM company')
            return conn.execute(statement).fetchall()
'''
