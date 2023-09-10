from sqlalchemy import create_engine, inspect, text
import pytest
from sqlalchemy.sql import text
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class CompanyTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_companies(self):        
        with self.db.connect() as conn:
            statement = text('SELECT * FROM company')
            return conn.execute(statement).fetchall()
        
    def get_active_companies(self):
        with self.db.connect() as conn:
            statement = text('SELECT * FROM company where is_active = true')
            return conn.execute(statement).fetchall()

    def delete_company(self, id):
        with self.db.connect() as conn:
            sql = text("delete from company where id = :id_to_delete")
            params = {"id_to_delete": id}
            conn.execute(sql, params)

    def create(self, name):
        with self.db.connect() as conn:
            params = {"new_name" : name}
            statement = text('insert into company(\"name\") values (:new_name)')
            return conn.execute(statement, params)

    def get_max_id(self):
        with self.db.connect() as conn:
            statement = text('select max(id) from company')
            return conn.execute(statement).fetchall()[0][0]


