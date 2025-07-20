def solve():
    """Index: 5572.
    Returns: the total number of presents Alicia got.
    """
    # L1
    small_presents = 10 # 10 of the presents were in small boxes
    medium_presents = 12 # 12 of the presents were in medium boxes
    known_presents = small_presents + medium_presents

    # L2
    known_parts_of_total = 2 # A third of all the presents she is given are in large boxes (implies 2/3 are small/medium)
    one_third_of_total_presents = known_presents / known_parts_of_total

    # L3
    total_parts = 3 # A third of all the presents she is given are in large boxes (implies total is 3 times one third)
    total_presents = one_third_of_total_presents * total_parts

    # FA
    answer = total_presents
    return answer