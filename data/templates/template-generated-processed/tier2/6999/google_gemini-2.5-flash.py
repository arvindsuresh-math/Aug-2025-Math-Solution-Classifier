def solve():
    """Index: 6999.
    Returns: the total pounds of vegetables James eats a week.
    """
    # L1
    asparagus_initial_weight_per_day = 0.25 # a quarter pound of asparagus
    broccoli_initial_weight_per_day = 0.25 # a quarter pound of broccoli
    initial_daily_vegetable_weight = asparagus_initial_weight_per_day + broccoli_initial_weight_per_day

    # L2
    doubling_factor = 2 # doubles that amount
    doubled_daily_vegetable_weight = initial_daily_vegetable_weight * doubling_factor

    # L3
    days_per_week = 7 # WK
    weekly_asparagus_broccoli_weight = doubled_daily_vegetable_weight * days_per_week

    # L4
    kale_weekly_weight = 3 # adds 3 pounds of kale per week
    total_weekly_vegetable_weight = weekly_asparagus_broccoli_weight + kale_weekly_weight

    # FA
    answer = total_weekly_vegetable_weight
    return answer