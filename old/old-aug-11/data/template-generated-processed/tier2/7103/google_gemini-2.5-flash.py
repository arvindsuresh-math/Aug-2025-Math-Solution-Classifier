def solve():
    """Index: 7103.
    Returns: the total cost Harry needed to pay for the balloons.
    """
    # L1
    total_balloons = 14 # exactly 14 balloons
    pack_size = 10 # pack of 10 balloons
    separate_balloons = total_balloons - pack_size

    # L2
    cost_per_single_balloon = 0.5 # One balloon costs $0.5
    cost_of_separate_balloons = separate_balloons * cost_per_single_balloon

    # L3
    cost_of_pack = 3 # costs only $3
    total_cost = cost_of_pack + cost_of_separate_balloons

    # FA
    answer = total_cost
    return answer