# weather/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    weather_data = relationship("WeatherData", back_populates="city")

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    city_id = Column(Integer, ForeignKey('cities.id'))

    city = relationship("City", back_populates="weather_data")
