from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
SQLALCHEMY_DATABASE_URL = "postgresql://zhzpvzruoasfks:2956c6212623be97d7cbef514ca7d387050dd799083ecd1b0d60254a020d53f3@ec2-34-230-198-12.compute-1.amazonaws.com:5432/d46uj9ac9lcdab"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
