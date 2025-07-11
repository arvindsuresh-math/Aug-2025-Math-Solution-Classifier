def solve():
    """Index: 1527.
    Returns: the number of balloons the clown is still holding.
    """
    # L1
    num_dozen_balloons = 3 # 3 dozen balloons
    dozen = 12 # WK
    initial_balloons = num_dozen_balloons * dozen

    # L2
    num_boys = 3 # 3 boys
    num_girls = 12 # 12 girls
    children_buying_balloons = num_boys + num_girls

    # L3
    remaining_balloons = initial_balloons - children_buying_balloons

    # FA
    answer = remaining_balloons
    return answer