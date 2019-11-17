from abc import ABC
from enum import Enum
from  types import Types

def gen_move_stats(base_power, accuracy, power_points):
    return {
        'base_power': base_power,
        'accuracy': accuracy,
        'power_points': power_points
    }

class MoveCategories(Enum):
    Physical=1
    Special=1
    Status=1

class Move:
    def __init__(self, moveType, moveCategory, stats):
        assert isinstance(moveType, Types)
        self.moveType = moveType
        self.stats = stats
    
    def use(self, stats):
        

tackle = Move(Types.Normal, MoveCategories.Physical, gen_move_stats(40, 100, 35))
        
