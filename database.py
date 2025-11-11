from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
url="postgresql://postgre:1234321@localhost:54321/man"
engine=create_engine(url)
session=sessionmaker(autocommit=False,autoflush=False,bind=engine)
