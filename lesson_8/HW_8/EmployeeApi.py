import requests
import random
from faker import Faker
import string

class EmployeeApi:
  

    def __init__(self, url):
        self.url = url

    def get_company_list(self, params_to_add = None):
        resp = requests.get(self.url +'/company', params= params_to_add) 
        return resp.json()
 
    def get_token(self, user = 'leonardo', password = 'leads' ):    
        creds = {
            'username' : user,
            'password' : password
        }
        resp = requests.post(self.url+'/auth/login', json=creds) 
        return resp.json()["userToken"]
    
    def generate_random_words(self, num_words):  
        fake = Faker()
        words = [fake.word() for _ in range(num_words)]
        return ' '.join(words)

    def generate_random_email(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        email = f"{random_string}@example.com"
        return email

    def generate_random_phone(self):
        phone = '+7' + ''.join(random.choices(string.digits, k=10))
        return phone
    
    def generate_random_url(self):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        url = f"https://example.com/{random_string}"
        return url
    
    def generate_random_birthdate(self):
        day = random.randint(1, 28)  # выбираем случайный день от 1 до 28
        month = random.randint(1, 12)  # выбираем случайный месяц от 1 до 12
        year = random.randint(1900, 2022)  # выбираем случайный год от 1900 до 2022
        birthdate = f"{year}-{month:02d}-{day:02d}"
        return birthdate

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
     
    '''
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
    '''       
    
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