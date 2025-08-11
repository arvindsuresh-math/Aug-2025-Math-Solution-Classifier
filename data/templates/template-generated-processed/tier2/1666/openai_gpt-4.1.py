def solve():
    """Index: 1666.
    Returns: the total amount Calvin has spent on chips after 4 weeks.
    """
    # L1
    chips_cost_per_bag = 0.50 # chips cost $0.50 a bag
    days_per_week = 5 # buys them 5 days a week
    weekly_spending = chips_cost_per_bag * days_per_week

    # L2
    num_weeks = 4 # over 4 weeks
    total_spending = weekly_spending * num_weeks

    # FA
    answer = total_spending
    return answer