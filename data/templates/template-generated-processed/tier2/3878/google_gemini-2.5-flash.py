def solve():
    """Index: 3878.
    Returns: the total money earned from candy bar sales.
    """
    # L1
    num_members = 20 # 20 members of a group
    avg_bars_per_member = 8 # an average of 8 candy bars
    total_candy_bars_sold = num_members * avg_bars_per_member

    # L2
    cost_per_bar = 0.50 # costs $0.50 each
    total_money_earned = total_candy_bars_sold * cost_per_bar

    # FA
    answer = total_money_earned
    return answer