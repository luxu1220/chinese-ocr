from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from constants import *

engine = create_engine(
    f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}'
    f'@{MYSQL_IP}/{MYSQL_DATABASE}?charset=utf8',
    max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)