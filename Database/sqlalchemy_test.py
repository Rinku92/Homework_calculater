from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

metadata = MetaData()
engine = create_engine('sqlite:////web/Sqlite-Data/example.db')

Base = declarative_base()

customers = Table('customers', metadata,
    Column('id', Integer(), primary_key=True),
    Column('first_name', String(100), nullable=False),
    Column('last_name', String(100), nullable=False),
    Column('username', String(50), nullable=False),
    Column('email', String(200), nullable=False),
    Column('address', String(200), nullable=False),
    Column('town', String(50), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)

metadata.create_all(engine)
