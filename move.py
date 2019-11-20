from abc import ABC
from enum import Enum
from monTypes import MonTypes
from effective import how_effective


class Move(ABC):
    def __init__(self, moveType, moveStats):
        assert isinstance(moveType, MonTypes)
        self.moveType = moveType
        self.moveStats = moveStats

    def use(self, user, opponent,  environment):
        raise NotImplementedError


class StatusMove(Move):
    def use(self, user, opponent, environment):
        raise NotImplementedError


class AttackMove(Move):
    def use(self, user, opponent, environment):
        assert self in user.moves

        # https://bulbapedia.bulbagarden.net/wiki/Damage
        damage = (2 * user.level / 5) + 2
        damage *= self.moveStats['base_power'] * user.stats[self.attack_name] / \
            opponent.stats[self.defense_name]
        damage = damage / 50 + 2

        modifier = 1

        # stab bonus
        if self.moveType in user.monTypes:
            modifier *= 1.5

        # effectiveness
        for monType in opponent.monTypes:
            modifier *= how_effective(self.moveType, monType)

        health = opponent.stats['health'] - damage * modifier
        if health < 0:
            health = 0
        opponent.stats['health'] = int(health)


class PhysicalMove(AttackMove):
    def __init__(self, moveType, moveStats):
        self.attack_name = 'attack'
        self.defense_name = 'defense'
        Move.__init__(self, moveType, moveStats)


class SpecialMove(AttackMove):
    def __init__(self, moveType, moveStats):
        self.attack_name = 'special_attack'
        self.defense_name = 'special_defense'
        Move.__init__(self, moveType, moveStats)
