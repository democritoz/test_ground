from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mariadb+mariadbconnector://root:qkrwlgh@mariadb_docker:3306/auto_trading")
print('engine=[', engine, ']')

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
print('db_session=[', db_session, ']')

Base = declarative_base()
print('Base=[', Base, ']')

Base.query = db_session.query_property()
print('Base.query=[', Base.query, ']')