from moveList import tackle,  pound
from monList import Charizard

if __name__ == '__main__':
    moves = [tackle, pound]
    mon1 = Charizard(moves, 36)
    mon2 = Charizard(moves, 40, nickname='Alex')
    tackle.use(mon1, mon2, None)
    print(mon2.stats)