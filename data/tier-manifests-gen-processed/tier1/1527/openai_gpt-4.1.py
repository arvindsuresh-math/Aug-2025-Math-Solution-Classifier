def solve():
    """Index: 1527.
    Returns: the number of balloons the clown is still holding after the children buy theirs.
    """
    # L1
    num_dozen = 3 # 3 dozen balloons
    dozen = 12 # WK
    total_balloons = num_dozen * dozen

    # L2
    num_boys = 3 # 3 boys
    num_girls = 12 # 12 girls
    total_kids = num_boys + num_girls

    # L3
    balloons_left = total_balloons - total_kids

    # FA
    answer = balloons_left
    return answer