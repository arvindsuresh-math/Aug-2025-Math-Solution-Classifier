def solve():
    """Index: 1727.
    Returns: the total profit Niko will make from reselling all socks.
    """
    # L1
    sock_cost = 2 # cost $2 each
    profit_percent = 25 # gain 25% profit
    percent_factor = 0.01 # WK
    profit_per_pair_first = sock_cost * profit_percent * percent_factor

    # L2
    num_first_pairs = 4 # four of the pairs
    total_profit_first = profit_per_pair_first * num_first_pairs

    # L3
    profit_per_pair_second = 0.2 # $0.2 profit each for the other 5 pairs
    num_second_pairs = 5 # other 5 pairs
    total_profit_second = profit_per_pair_second * num_second_pairs

    # L4
    total_profit = total_profit_first + total_profit_second

    # FA
    answer = total_profit
    return answer