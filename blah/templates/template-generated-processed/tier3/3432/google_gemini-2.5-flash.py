def solve():
    """Index: 3432.
    Returns: the number of water balloons Floretta is left with.
    """
    # L1
    milly_floretta_packs = 3 # 3 packs of their own water balloons
    neighbor_packs = 2 # 2 packs of a neighbor’s water balloons
    total_packs = milly_floretta_packs + neighbor_packs

    # L2
    balloons_per_pack = 6 # Each pack of water balloons contains 6 balloons
    total_balloons = total_packs * balloons_per_pack

    # L3
    split_divisor = 2 # split them evenly
    balloons_per_person = total_balloons / split_divisor

    # L4
    milly_stolen_balloons = 7 # Milly takes an extra 7 balloons
    floretta_balloons_remaining = balloons_per_person - milly_stolen_balloons

    # FA
    answer = floretta_balloons_remaining
    return answer