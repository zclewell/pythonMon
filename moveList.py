from move import StatusMove, PhysicalMove, SpecialMove
from monTypes import MonTypes


def gen_attack_move_stats(base_power, accuracy, power_points):
    return {
        'base_power': base_power,
        'accuracy': accuracy,
        'power_points': power_points
    }


def gen_status_move_stats(health, speed, attack, defense, special_attack, special_defense):
    return {
        'health': health,
        'speed': speed,
        'attack': attack,
        'defense': defense,
        'special_attack': special_attack,
        'special_defense': special_defense
    }


class Tackle(PhysicalMove):
    def __init__(self):
        PhysicalMove.__init__(self, MonTypes.Normal, gen_attack_move_stats(40, 100, 35))


class Pound(PhysicalMove):
    def __init__(self):
        PhysicalMove.__init__(self, MonTypes.Normal,
                              gen_attack_move_stats(40, 100, 35))

class Ember(SpecialMove):
    def __init__(self):
        PhysicalMove.__init__(self, MonTypes.Fire,
                              gen_attack_move_stats(40, 100, 25))

class JumpKick(PhysicalMove):
    def __init__(self):
        PhysicalMove.__init__(self, MonTypes.Fighting,
                              gen_attack_move_stats(100, 95, 10))




