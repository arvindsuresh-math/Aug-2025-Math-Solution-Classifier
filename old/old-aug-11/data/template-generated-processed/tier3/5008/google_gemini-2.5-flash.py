def solve():
    """Index: 5008.
    Returns: the total number of gumballs in the machine.
    """
    # L1
    red_gumballs = 16 # 16 red gumballs
    blue_gumball_divisor = 2 # half as many blue gumballs
    blue_gumballs = red_gumballs / blue_gumball_divisor

    # L2
    green_gumball_multiplier = 4 # 4 times as many green gumballs
    green_gumballs = blue_gumballs * green_gumball_multiplier

    # L3
    total_gumballs = red_gumballs + green_gumballs + blue_gumballs

    # FA
    answer = total_gumballs
    return answer