def solve():
    """Index: 2855.
    Returns: the total money Erica spends on ice cream in 6 weeks.
    """
    # L1
    creamsicle_days_per_week = 3 # Monday, Wednesday and Friday
    creamsicle_cost_per_day = 2.00 # $2.00 orange creamsicle
    creamsicle_weekly_cost = creamsicle_days_per_week * creamsicle_cost_per_day

    # L2
    sandwich_days_per_week = 2 # Tuesday and Thursday
    sandwich_cost_per_day = 1.50 # $1.50 ice cream sandwich
    sandwich_weekly_cost = sandwich_days_per_week * sandwich_cost_per_day

    # L3
    nutty_buddy_days_per_week = 2 # Saturday and Sunday
    nutty_buddy_cost_per_day = 3.00 # $3.00 Nutty-Buddy
    nutty_buddy_weekly_cost = nutty_buddy_days_per_week * nutty_buddy_cost_per_day

    # L4
    total_weekly_cost = creamsicle_weekly_cost + sandwich_weekly_cost + nutty_buddy_weekly_cost

    # L5
    num_weeks = 6 # For 6 weeks in the summer
    total_cost_6_weeks = num_weeks * total_weekly_cost

    # FA
    answer = total_cost_6_weeks
    return answer