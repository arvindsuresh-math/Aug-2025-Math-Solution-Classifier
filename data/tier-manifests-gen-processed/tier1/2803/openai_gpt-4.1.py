def solve():
    """Index: 2803.
    Returns: the amount of money in dollars Todd has left after buying the candy bars.
    """
    # L1
    num_candy_bars = 4 # 4 candy bars
    cost_per_bar = 2 # cost $2 each
    total_candy_cost = num_candy_bars * cost_per_bar

    # L2
    todd_initial_money = 20 # Todd has $20
    todd_money_left = todd_initial_money - total_candy_cost

    # FA
    answer = todd_money_left
    return answer