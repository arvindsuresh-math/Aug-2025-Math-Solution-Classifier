def solve():
    """Index: 1727.
    Returns: Niko's total profit.
    """
    # L1
    cost_per_pair_socks = 2 # $2 each
    profit_percent_num = 25 # 25% profit
    percent_divisor = 100 # WK
    profit_per_first_four_pair = cost_per_pair_socks * profit_percent_num / percent_divisor

    # L2
    num_first_four_pairs = 4 # four of the pairs of socks
    total_profit_first_four_pairs = profit_per_first_four_pair * num_first_four_pairs

    # L3
    profit_per_other_pair = 0.2 # $0.2 profit each
    num_other_five_pairs = 5 # other 5 pairs of socks
    total_profit_other_five_pairs = profit_per_other_pair * num_other_five_pairs

    # L4
    total_profit = total_profit_first_four_pairs + total_profit_other_five_pairs

    # FA
    answer = total_profit
    return answer