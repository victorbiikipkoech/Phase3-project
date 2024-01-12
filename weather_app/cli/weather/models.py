# weather/models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer)
    timestamp = Column(DateTime, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))
    city = relationship('City', back_populates='weather_data')

City.weather_data = relationship('WeatherData', order_by=WeatherData.timestamp, back_populates='city')
