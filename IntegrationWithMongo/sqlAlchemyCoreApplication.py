from sqlalchemy import create_engine, Integer, String, text, Engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import ForeignKey

engine = create_engine('sqlite://')
metadata_obj = MetaData()
user = Table(
    'user', metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('email_address', String(60)),
    Column('user_name', String(40), nullable=False),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefs', metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'), nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100))
)

# for table in metadata_obj.sorted_tables:
#     print(table)

metadata_bd_obj = MetaData()
financial_info = Table(
    'financial_info', metadata_bd_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False)
)

