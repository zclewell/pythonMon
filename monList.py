from mon import Mon, gen_mon_stats
from moveList import tackle, pound
from monTypes import MonTypes


class Charizard(Mon):
    def __init__(self, moves, level, nickname=False, stats=False):
        if nickname:
            name = nickname
        else:
            name = 'Charizard'
        if not stats:
            stats = gen_mon_stats(90, 90, 90, 90, 90, 90)
        Mon.__init__(self, name, stats, [
            MonTypes.Fire, MonTypes.Flying], moves, level)
