from move import StatusMove, PhysicalMove, SpecialMove
from monTypes import MonTypes


def gen_move_stats(base_power, accuracy, power_points):
    return {
        'base_power': base_power,
        'accuracy': accuracy,
        'power_points': power_points
    }


tackle = PhysicalMove(MonTypes.Normal,
                      gen_move_stats(40, 100, 35))
pound = PhysicalMove(MonTypes.Normal,
                     gen_move_stats(40, 100, 35))
