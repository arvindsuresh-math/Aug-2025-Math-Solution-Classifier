def solve():
    """Index: 2746.
    Returns: the weight of Carl.
    """
    # L1
    ed_weight = 146 # Ed weighs 146 pounds
    al_heavier_than_ed = 38 # 38 pounds lighter than Al
    al_weight = ed_weight + al_heavier_than_ed

    # L2
    al_heavier_than_ben = 25 # Al is 25 pounds heavier than Ben
    ben_weight = al_weight - al_heavier_than_ben

    # L3
    ben_lighter_than_carl = 16 # Ben is 16 pounds lighter than Carl
    carl_weight = ben_weight + ben_lighter_than_carl

    # FA
    answer = carl_weight
    return answer