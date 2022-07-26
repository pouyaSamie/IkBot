from sqlalchemy import Column, Integer,BIGINT
from Data.base import Base

class DragonGoldCost(Base):
    __tablename__ = 'dragon_gold_cost'
    id = Column(Integer, primary_key=True)
    level = Column(Integer)
    gold_cost = Column(BIGINT)

    def __init__(self, level, gold_cost):
        self.level = level
        self.gold_cost = gold_cost