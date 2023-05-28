from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import func


base = declarative_base()

class User(base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        'Address', back_populates='User'
    )
    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, fullname={self.fullname})'

class Address(base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    User_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    User = relationship('User', back_populates='address')

    def __repr__(self):
        return f'address(id={self.id}, email={self.email_address})'


# conexão DB

engine = create_engine('sqlite://')

# criando tabelas no BD

base.metadata.create_all(engine)

# inspetor

inspetor_engine = inspect(engine)
# print(inspetor_engine.has_table('user_account'))
# print(inspetor_engine.get_table_names())
# print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name='Juliana',
        fullname='Juliiana Silva',
        address=[Address(email_address='juliananame@email.com')]
    )

    sandy = User(
        name='Sandy',
        fullname="Sandy Santos",
        address=[Address(email_address='sandyname@email.com'),
                 Address(email_address='sandy123@email.com')]
    )

    patrick = User(
        name='Patrick',
        fullname="Patrick Santos"
    )

    #enviando para o BD
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['Juliana', 'Sandy']))
# for user in session.scalars(stmt):
#     print(user)

stmt_address = select(Address).where(Address.User_id.in_([2]))
# for address in session.scalars(stmt_address):
#     print(address)

order_stmt = select(User).order_by(User.fullname.desc())
# print('\nRecuperando infos de maneira ordenada\n')
# for result in session.scalars(order_stmt):
#     print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)

# for result in session.scalars(stmt_join):
#     print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()

# print('\nExecutando o statement a partir da connection\n')
# for result in results:
#     print(result)

# Total de instâncias em User
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
     print(result)