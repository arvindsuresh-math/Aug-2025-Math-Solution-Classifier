def solve():
    """Index: 6035.
    Returns: the total money Cherry will earn in a week.
    """
    # L1
    charge_3_5kg_cargo = 2.50 # $2.50 for a 3-5 kilograms cargo
    num_5kg_cargo_per_day = 4 # four 5 kilograms cargo
    earnings_5kg_cargo_per_day = charge_3_5kg_cargo * num_5kg_cargo_per_day

    # L2
    charge_6_8kg_cargo = 4 # $4 for a 6-8 kilograms cargo
    num_8kg_cargo_per_day = 2 # two 8 kilograms cargo
    earnings_8kg_cargo_per_day = charge_6_8kg_cargo * num_8kg_cargo_per_day

    # L3
    total_daily_earnings = earnings_8kg_cargo_per_day + earnings_5kg_cargo_per_day

    # L4
    days_per_week = 7 # in a week
    weekly_earnings = total_daily_earnings * days_per_week

    # FA
    answer = weekly_earnings
    return answer