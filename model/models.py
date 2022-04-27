from sqlalchemy import Column, Integer, TEXT, REAL, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class VideoGame(Base):
    __tablename__ = "video_game"
    GameID = Column(Integer, primary_key=True)
    Name = Column(TEXT)
    Platform = Column(TEXT)
    Year = Column(Integer)
    Genre = Column(TEXT)
    Publisher = Column(TEXT)

    def __repr__(self):
        return f"VideoGame({self.GameID}, {self.Name}, {self.Platform}, {self.Year}, {self.Genre}, {self.Publisher})"


class Sale(Base):
    __tablename__ = "sales"
    GameID = Column(Integer, primary_key=True)
    NA_Sales_in_millions = Column(REAL)
    EU_Sales_in_millions = Column(REAL)
    JP_Sales_in_millions = Column(REAL)
    Other_Sales_in_millions = Column(REAL)
    Global_Sales_in_millions = Column(REAL)

    def __repr__(self):
        return f"Sale({self.GameID}, {self.NA_Sales_in_millions}, {self.EU_Sales_in_millions}" \
               f", {self.JP_Sales_in_millions}, {self.Other_Sales_in_millions}" \
               f", {self.Global_Sales_in_millions})"
