from sqlalchemy import ForeignKey, create_engine, Table, Column, MetaData, Integer, String
from sqlalchemy_utils import create_database, database_exists


engine = create_engine('sqlite:///sqlalchemy/database.db')

# Create database
if not database_exists(engine.url):
    create_database(engine.url)

convention = {
  'ix': 'ix_%(column_0_label)s',
  'uq': 'uq_%(table_name)s_%(column_0_name)s',
  'ck': 'ck_%(table_name)s_%(constraint_name)s',
  'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
  'pk': 'pk_%(table_name)s'
}

metadata = MetaData(engine, naming_convention=convention)

user_table = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(100), nullable=False),
    Column('password', String(100), nullable=False),
    Column('first_name', String(100)),
    Column('last_name', String(100))
)


post_table = Table(
    'post',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(200), nullable=False),
    Column('text', String),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False)
)

metadata.create_all(engine)