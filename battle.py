from moveList import *
from monList import Charizard
from graphics import show_moves, Colors, show_use_attack, show_use_status, show_miss
from move import PriorityMove, StatusMove


class SelectedMove:
    def __init__(self, move, user, oppt):
        self.move  = move
        self.user =  user
        self.oppt = oppt
        self.used = False

    def use(self, environment):
        if isinstance(self.move, StatusMove):
            show_use_status(self)
        else:
            show_use_attack(self)
        hit = self.move.use(self.user, self.oppt, environment)
        if not hit:
            show_miss()

        self.used = True

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

    def take_turn(self, mon):
        if mon is self.mon1:
            user = mon1
            oppt = mon2
            color = Colors.colors['RED']
        else:
            user = mon2
            oppt = mon1
            color = Colors.colors['BLUE']
        self.mon1_turn = not self.mon1_turn
        show_moves(mon, color)

        # get user selection
        index = int(input())
        moves = mon.moves
        while index < 0 or index >= len(moves):
            index = int(input('Invalid, try again'))

        move = moves[index]
        return SelectedMove(move, user, oppt)

    def process_turn(self, mon1, move1, mon2,  move2):
        if isinstance(move1, PriorityMove) or isinstance(move2, PriorityMove):
            pass  # Quick Attack etc.

        speed1 = mon1.stats['speed']
        speed2 = mon2.stats['speed']

        environment = self.environment
        if speed1 > speed2:
            if not move1.used:
                move1.use(environment)
            if not move2.used:
                move2.use(environment)
        else:
            if not move2.used:
                move2.use(environment)
            if not move1.used:
                move1.use(environment)

    def start(self):
        with self.mon1, self.mon2:
            while not self._is_over():
                move1 = self.take_turn(self.mon1)
                move2 = self.take_turn(self.mon2)
                self.process_turn(self.mon1, move1, self.mon2, move2)


if __name__ == '__main__':
    moves1 = [Tackle(), Pound(), Ember(), JumpKick()]
    mon1 = Charizard(moves1, 36)
    moves2 = [Tackle(), Pound()]
    mon2 = Charizard(moves2, 40, nickname='Alex')
    battle = Battle(mon1, mon2)
    battle.start()
