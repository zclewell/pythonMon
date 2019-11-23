from abc import ABC
from enum import Enum
from monTypes import MonTypes
from effective import how_effective


class Move:
    def  __init__(self):
        pass

    def use(self):
        self.move_stats['power_points'] -= 1

class StatusMove(Move):
    def __init__(self, move_type, move_stats):
        self.move_type = move_type
        self.move_stats = move_stats

    def use(self, user, target, environment):
        assert self in user.moves
        target.stats['health'] *= self.move_stats['health']
        target.stats['speed'] *= self.move_stats['speed']
        target.stats['attack'] *= self.move_stats['attack']
        target.stats['defense'] *= self.move_stats['defense']
        target.stats['special_attack'] *= self.move_stats['special_attack']
        target.stats['special_defense'] *= self.move_stats['special_defense']
        Move.use(self)


class AttackMove(Move):
    def __init__(self, move_type, move_stats):
        assert isinstance(move_type, MonTypes)
        self.move_type = move_type
        self.move_stats = move_stats

    def use(self, user, target, environment):

        # https://bulbapedia.bulbagarden.net/wiki/Damage
        damage = (2 * user.level / 5) + 2
        damage *= self.move_stats['base_power'] * user.stats[self.attack_name] / \
            target.stats[self.defense_name]
        damage = damage / 50 + 2

        modifier = 1

        # stab bonus
        if self.move_type in user.monTypes:
            modifier *= 1.5

        # effectiveness
        for monType in target.monTypes:
            modifier *= how_effective(self.move_type, monType)

        health = target.stats['health'] - damage * modifier
        if health < 0:
            health = 0
        target.stats['health'] = int(health)
        Move.use(self)


class PhysicalMove(AttackMove):
    def __init__(self, move_type, move_stats):
        self.attack_name = 'attack'
        self.defense_name = 'defense'
        AttackMove.__init__(self, move_type, move_stats)


class SpecialMove(AttackMove):
    def __init__(self, move_type, move_stats):
        self.attack_name = 'special_attack'
        self.defense_name = 'special_defense'
        AttackMove.__init__(self, move_type, move_stats)
