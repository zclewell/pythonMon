from move import Move, MoveCategories, gen_move_stats
from monTypes import MonTypes

tackle = Move(MonTypes.Normal, MoveCategories.Physical,
              gen_move_stats(40, 100, 35))
pound = Move(MonTypes.Normal, MoveCategories.Physical,
             gen_move_stats(40, 100, 35))
