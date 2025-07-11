def solve():
    """Index: 1666.
    Returns: the total money Calvin has spent on chips.
    """
    # L1
    chip_cost_per_bag = 0.50 # $0.50
    days_per_week_bought = 5 # 5 days a week
    weekly_cost = chip_cost_per_bag * days_per_week_bought

    # L2
    num_weeks = 4 # After 4 weeks
    total_cost = weekly_cost * num_weeks

    # FA
    answer = total_cost
    return answer