import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)  
sys.path.append(parent_directory)

from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
import databases
from settings.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker

database = databases.Database(DATABASE_URL)
Base = declarative_base()

async def db_connect():
    await database.connect()
    return database