def solve():
    """Index: 968.
    Returns: the total number of shirts Mary has left.
    """
    # L1
    initial_blue_shirts = 26 # 26 blue shirts
    blue_shirts_divisor = 2 # half of her blue shirts
    given_away_blue_shirts = initial_blue_shirts / blue_shirts_divisor

    # L2
    initial_brown_shirts = 36 # 36 brown shirts
    brown_shirts_divisor = 3 # a third of her brown shirts
    given_away_brown_shirts = initial_brown_shirts / brown_shirts_divisor

    # L3
    remaining_blue_shirts = initial_blue_shirts - given_away_blue_shirts

    # L4
    remaining_brown_shirts = initial_brown_shirts - given_away_brown_shirts

    # L5
    total_shirts_left = remaining_blue_shirts + remaining_brown_shirts

    # FA
    answer = total_shirts_left
    return answer