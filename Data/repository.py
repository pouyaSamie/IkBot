from sqlalchemy import BIGINT
from Data.dragon_gold_cost import DragonGoldCost
from Data.base import Session

def GetAllDragons(level):
    session = Session()
    dragon = session.query(DragonGoldCost) \
              .filter(DragonGoldCost.level == level).first()
    return dragon
