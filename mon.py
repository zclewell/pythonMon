from abc import ABC
from move import Move, MoveCategories
from monTypes import MonTypes


def gen_mon_stats(health, speed, attack, defense, special_attack, special_defense):
    return {
        'health': health,
        'speed': speed,
        'attack': attack,
        'defense': defense,
        'special_attack': special_attack,
        'special_defense': special_defense
    }


class Mon(ABC):
    def __init__(self, name, stats, monTypes, moves, level):
        assert len(moves) <= 4 and len(moves) >= 1
        for move in moves:
            assert isinstance(move, Move)
        assert len(monTypes) <= 2 and len(monTypes) >= 1
        for monType in monTypes:
            assert isinstance(monType, MonTypes)
        self.name = name
        self.stats = stats
        self.moves = moves
        self.level = level

    def __enter__(self):
        print('{} Lv. {} joined the battle!'.format(self.name, self.level))

    def __exit__(self, type, value, tb):
        pass

    def use_move(self, move, opponent, environment):
        assert move in self.moves

        # TODO this always returns true?!
        # if move.moveCategory is MoveCategories.Status:
        #     return

        # https: // bulbapedia.bulbagarden.net/wiki/Damage
        damage = (2 * self.level / 5) + 2
        if move.moveCategory == MoveCategories.Physical:
            damage *= move.moveStats['base_power'] * self.stats['attack'] / \
                opponent.stats['defense']
        elif move.moveCategory == MoveCategories.Special:
            damage *= move.moveStats['base_power'] * self.stats['special_attack'] / \
                opponent.stats['special_defense']
        damage = damage / 50 + 2

        health = opponent.stats['health'] - damage
        if health < 0:
            health = 0
        opponent.stats['health'] = int(health)
