from abc import ABC
from move import Move, tackle

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
    def __init__(self, name, stats, moves, type):
        assert len(moves) <= 4 and len(moves) >= 1
        for move in moves:
            assert isinstance(move, Move)
        self.name = name
        self.stats = stats
        self.moves = moves

    def __enter__(self):
        print('{} joined the battle!'.format(self.name))

    def __exit__(self, type, value, tb):
        pass

    def use_move(self, opponent, move):
        assert move in self.moves
        # switch on move type?

    def recieve_move(self, move):
        self.stats = move.use(self.stats)

class Charizard(Mon):
    def  __init__(self, nickname=False, stats=False):
        if nickname:
            name = nickname
        else:
            name = 'Charizard'
        if not stats:
            stats = gen_mon_stats(90, 90, 90, 90, 90, 90)
        super(Charizard, self).__init__(name, stats)    

if __name__ == '__main__':
    with Charizard():
        pass
    with Charizard('alex'):
        pass
