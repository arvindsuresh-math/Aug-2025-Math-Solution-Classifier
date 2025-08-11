def solve():
    """Index: 2024.
    Returns: the number of balloons left after some burst.
    """
    # L1
    red_balloons = 20 # 20 red balloons
    green_balloons = 15 # 15 green balloons
    total_initial_balloons = red_balloons + green_balloons

    # L2
    burst_red = 3 # 3 red ... balloons burst
    burst_green = 2 # 2 green balloons burst
    total_burst_balloons = burst_red + burst_green

    # L3
    balloons_left = total_initial_balloons - total_burst_balloons

    # FA
    answer = balloons_left
    return answer