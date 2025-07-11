def solve():
    """Index: 2024.
    Returns: the number of balloons left after some burst before the party.
    """
    # L1
    red_balloons = 20 # 20 red balloons
    green_balloons = 15 # 15 green balloons
    total_balloons = red_balloons + green_balloons

    # L2
    red_burst = 3 # 3 red ... burst
    green_burst = 2 # 2 green ... burst
    total_burst = red_burst + green_burst

    # L3
    balloons_left = total_balloons - total_burst

    # FA
    answer = balloons_left
    return answer