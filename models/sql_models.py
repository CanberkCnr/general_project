from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class ExampleData(Base):
    __tablename__ = 'example_date'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    day = Column(Date, nullable=False)
    temperature_max = Column(Float, nullable=False)
    temperature_min = Column(Float, nullable=False)
    average_temperature = Column(Float, nullable=False)
