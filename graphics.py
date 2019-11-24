class Colors:
    colors = {}
    colors['RED'] = '\033[31m'
    colors['BLUE'] = '\033[34m'
    colors['_END'] = '\033[0m'

    colors['Normal'] = ''
    colors['Fire'] = '\033[31m'
    colors['Fighting'] = '\033[88m'
    colors['Water'] = '\033[m'
    colors['Flying'] = '\033[m'
    colors['Grass'] = '\033[m'
    colors['Poison'] = '\033[m'
    colors['Electric'] = '\033[m'
    colors['Ground'] = '\033[m'
    colors['Psychic'] = '\033[m'
    colors['Rock'] = '\033[m'
    colors['Ice'] = '\033[m'
    colors['Bug'] = '\033[m'
    colors['Dragon'] = '\033[m'
    colors['Ghost'] = '\033[m'
    colors['Dark'] = '\033[m'
    colors['Steel'] = '\033[m'
    colors['Fairy'] = '\033[m'
    
    @staticmethod
    def colorize(word, color):
        return '{}{}{}'.format(
            color,
            word,
            Colors.colors['_END']
        )
    
    @staticmethod
    def color_type(name):
        return Colors.colorize(
            name,
            Colors.colors[name]
        )


def show_moves(mon, color):
    print("{}'s turn, select a move".format(
            Colors.colorize(mon.name, color)))
    moves = mon.moves
    for idx, move in enumerate(moves):
        print('{}: {} - {} ({})'.format(idx,
                                        move.__class__.__name__,
                                        Colors.color_type(move.move_type.name),
                                        move.move_stats['power_points']))


