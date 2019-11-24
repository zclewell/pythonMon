from moveList import *
from monList import Charizard
from graphics import show_moves, Colors



class Battle:
    def __init__(self, mon1, mon2):
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon1_turn = True
        self.environment = {}

    def _is_over(self):
        mon1_health = self.mon1.stats['health']
        mon2_health = self.mon2.stats['health']
        return mon1_health <= 0 or mon2_health <= 0

    def take_turn(self):
        if self.mon1_turn:
            user = self.mon1
            oppt = self.mon2
            color = Colors.colors['RED']
        else:
            user = self.mon2
            oppt = self.mon1
            color = Colors.colors['BLUE']
        self.mon1_turn = not self.mon1_turn
        show_moves(user, color)
        index = int(input())
        moves = user.moves
        while index < 0 or index >= len(moves):
            index = int(input('Invalid, try again'))
        user.use_move(moves[index], oppt, self.environment)

    def start(self):
        with self.mon1, self.mon2:
            while not self._is_over():
                self.take_turn()


if __name__ == '__main__':
    moves1 = [Tackle(), Pound(), Ember(), JumpKick()]
    mon1 = Charizard(moves1, 36)
    moves2 = [Tackle(), Pound()]
    mon2 = Charizard(moves2, 40, nickname='Alex')
    battle = Battle(mon1, mon2)
    battle.start()
