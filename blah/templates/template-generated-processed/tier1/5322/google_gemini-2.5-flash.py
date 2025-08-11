def solve():
    """Index: 5322.
    Returns: the number of fish Harry has.
    """
    # L1
    joe_multiplier = 8 # 8 times as many fish as Sam
    sam_fish = 7 # Sam has 7 fish
    joe_fish = joe_multiplier * sam_fish

    # L2
    harry_multiplier = 4 # 4 times as many fish as Joe
    harry_fish = harry_multiplier * joe_fish

    # FA
    answer = harry_fish
    return answer