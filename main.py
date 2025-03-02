from sqlalchemy import create_engine,Column,String,Integer,REAL,CheckConstraint
from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy.ext.hybrid import hybrid_property

database_file = "database.db"
engine = create_engine(f"sqlite:///{database_file}")
