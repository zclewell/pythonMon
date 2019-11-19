from monTypes import MonTypes


def how_effective(move_type, opp_type):
    assert move_type in MonTypes
    assert opp_type in MonTypes

    super_effective = 2
    effective = 1
    not_very_effective =  0.5
    not_effective = 0

    if opp_type is MonTypes.Normal:
        if move_type is MonTypes.Fighting:
            return super_effective
        if move_type is MonTypes.Ghost:
            return not_effective

    if opp_type is MonTypes.Fighting:
        if move_type is MonTypes.Flying:
            return super_effective
        if move_type is MonTypes.Rock:
            return not_very_effective
        if move_type is MonTypes.Bug:
            return not_very_effective
        if move_type is MonTypes.Ghost:
            return super_effective
        if move_type is MonTypes.Psychic:
            return super_effective
        if move_type is MonTypes.Dark:
            return not_very_effective
        if move_type is MonTypes.Fairy:
            return super_effective

    if opp_type is MonTypes.Flying:
        if move_type is MonTypes.Fighting:
            return not_very_effective
        if move_type is MonTypes.Ground:
            return not_effective
        if move_type is MonTypes.Rock:
            return super_effective
        if move_type is MonTypes.Bug:
            return not_very_effective
        if move_type is MonTypes.Grass:
            return not_very_effective
        if move_type is MonTypes.Electric:
            return super_effective
        if move_type is MonTypes.Fairy:
            return not_very_effective

    if opp_type is MonTypes.Poison:
        if move_type is MonTypes.Fighting:
            return not_very_effective
        if move_type is MonTypes.Poison:
            return not_very_effective
        if move_type is MonTypes.Ground:
            return super_effective
        if move_type is MonTypes.Bug:
            return not_very_effective
        if move_type is MonTypes.Grass:
            return not_very_effective
        if move_type is MonTypes.Psychic:
            return super_effective
        if move_type is MonTypes.Fairy:
            return not_very_effective

    if opp_type is MonTypes.Ground:
        if move_type is MonTypes.Poison:
            return not_very_effective
        if move_type is MonTypes.Rock:
            return not_very_effective
        if move_type is MonTypes.Water:
            return super_effective
        if move_type is MonTypes.Grass:
            return super_effective
        if move_type is MonTypes.Electric:
            return not_effective
        if move_type is MonTypes.Ice:
            return super_effective

    if opp_type is MonTypes.Rock:
        if move_type is MonTypes.Normal:
            return not_very_effective
        if move_type is MonTypes.Fighting:
            return super_effective
        if move_type is MonTypes.Flying:
            return not_very_effective
        if move_type is MonTypes.Poison:
            return not_very_effective
        if move_type is MonTypes.Ground:
            return super_effective
        if move_type is MonTypes.Steel:
            return super_effective
        if move_type is MonTypes.Fire:
            return not_very_effective
        if move_type is MonTypes.Water:
            return super_effective
        if move_type is MonTypes.Grass:
            return  super_effective


    return effective
