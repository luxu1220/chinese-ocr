import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class Ocr(Base):
    __tablename__ = 'Ocr'
    id = Column(Integer, primary_key=True)
    image_file_name = Column(String(42), index=True)
    ocr_result = Column(String(500))
    create_time = Column(DateTime, default=datetime.datetime.now)
