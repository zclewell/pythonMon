class Colors:
    colors = {}
    colors['RED'] = '\033[31m'
    colors['BLUE'] = '\033[34m'
    colors['_END'] = '\033[0m'

    # http://www.epidemicjohto.com/t882-type-colors-hex-colors
    colors['Normal'] = '\033[48:2:168:167:122m'
    colors['Fire'] = '\033[48:2:238:129:48m'
    colors['Fighting'] = '\033[48:2:194:46:40m'
    colors['Water'] = '\033[48:2:99:144:240m'
    colors['Flying'] = '\033[48:2:169:143:243m'
    colors['Grass'] = '\033[48:2:122:199:76m'
    colors['Poison'] = '\033[48:2:163:62:161m'
    colors['Electric'] = '\033[48:2:247:208:44m'
    colors['Ground'] = '\033[48:2:226:191:101m'
    colors['Psychic'] = '\033[48:2:249:85:135m'
    colors['Rock'] = '\033[48:2:182:161:54m'
    colors['Ice'] = '\033[48:2:150:217:214m'
    colors['Bug'] = '\033[48:2:166:185:26m'
    colors['Dragon'] = '\033[48:2:111:53:252m'
    colors['Ghost'] = '\033[48:2:115:87:151m'
    colors['Dark'] = '\033[48:2:112:87:70m'
    colors['Steel'] = '\033[48:2:183:183:206m'
    colors['Fairy'] = '\033[48:2:214:133:173m'

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
            ' {} '.format(name),
            Colors.colors[name]
        )


def show_use_attack(selectedMove):
    print('{} used {}!'.format(
        selectedMove.user.name,
        selectedMove.move.__class__.__name__
    ))
    pass


def show_use_status(selectedMove):
    pass


def show_miss():
    print('It missed!')


def show_moves(mon, color):
    print("{}'s turn, select a move".format(
        Colors.colorize(mon.name, color)))
    moves = mon.moves
    for idx, move in enumerate(moves):
        print('{}: {} - {} ({})'.format(idx,
                                        move.__class__.__name__,
                                        Colors.color_type(move.move_type.name),
                                        move.move_stats['power_points']))
