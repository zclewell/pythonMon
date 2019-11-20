from abc import ABC
from enum import Enum
from monTypes import MonTypes
from effective import how_effective


class StatusMove:
    def __init__(self, moveType, statusChanges):
        self.moveType = moveType
        self.statusChanges = statusChanges

    def use(self, user, target, environment):
        assert self in user.moves
        target.stats['health'] *= self.statusChanges['health']
        target.stats['speed'] *= self.statusChanges['speed']
        target.stats['attack'] *= self.statusChanges['attack']
        target.stats['defense'] *= self.statusChanges['defense']
        target.stats['special_attack'] *= self.statusChanges['special_attack']
        target.stats['special_defense'] *= self.statusChanges['special_defense']


class AttackMove:
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
