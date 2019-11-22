from abc import ABC
from enum import Enum
from monTypes import MonTypes
from effective import how_effective


class Move:
    def  __init__(self):
        pass

    def use(self):
        self.moveStats['power_points'] -= 1

class StatusMove(Move):
    def __init__(self, moveType, moveStats):
        self.moveType = moveType
        self.moveStats = moveStats

    def use(self, user, target, environment):
        assert self in user.moves
        target.stats['health'] *= self.moveStats['health']
        target.stats['speed'] *= self.moveStats['speed']
        target.stats['attack'] *= self.moveStats['attack']
        target.stats['defense'] *= self.moveStats['defense']
        target.stats['special_attack'] *= self.moveStats['special_attack']
        target.stats['special_defense'] *= self.moveStats['special_defense']
        Move.use(self)


class AttackMove(Move):
    def __init__(self, moveType, moveStats):
        assert isinstance(moveType, MonTypes)
        self.moveType = moveType
        self.moveStats = moveStats

    def use(self, user, target, environment):
        assert self in user.moves

        # https://bulbapedia.bulbagarden.net/wiki/Damage
        damage = (2 * user.level / 5) + 2
        damage *= self.moveStats['base_power'] * user.stats[self.attack_name] / \
            target.stats[self.defense_name]
        damage = damage / 50 + 2

        modifier = 1

        # stab bonus
        if self.moveType in user.monTypes:
            modifier *= 1.5

        # effectiveness
        for monType in target.monTypes:
            modifier *= how_effective(self.moveType, monType)

        health = target.stats['health'] - damage * modifier
        if health < 0:
            health = 0
        target.stats['health'] = int(health)
        Move.use(self)


class PhysicalMove(AttackMove):
    def __init__(self, moveType, moveStats):
        self.attack_name = 'attack'
        self.defense_name = 'defense'
        AttackMove.__init__(self, moveType, moveStats)


class SpecialMove(AttackMove):
    def __init__(self, moveType, moveStats):
        self.attack_name = 'special_attack'
        self.defense_name = 'special_defense'
        AttackMove.__init__(self, moveType, moveStats)
