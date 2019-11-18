from abc import ABC
from enum import Enum
from monTypes import MonTypes


def gen_move_stats(base_power, accuracy, power_points):
    return {
        'base_power': base_power,
        'accuracy': accuracy,
        'power_points': power_points
    }


class MoveCategories(Enum):
    Physical = 1
    Special = 1
    Status = 1


class Move:
    def __init__(self, moveType, moveCategory, moveStats):
        assert isinstance(moveType, MonTypes)
        self.moveType = moveType
        self.moveStats = moveStats
        self.moveCategory = moveCategory

    def use(self, stats):
        assert self.moveStats['power_points'] > 0
