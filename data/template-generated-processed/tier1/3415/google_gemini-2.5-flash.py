def solve():
    """Index: 3415.
    Returns: the total money Jose will earn per week.
    """
    # L1
    charge_per_kid = 3 # charges $3 for kids
    num_kids_per_day = 8 # 8 kids swim in his swimming pool per day
    earnings_per_day_kids = charge_per_kid * num_kids_per_day

    # L2
    multiplier_adult_charge = 2 # twice that amount for adults
    charge_per_adult = charge_per_kid * multiplier_adult_charge

    # L3
    num_adults_per_day = 10 # 10 adults swim in his swimming pool per day
    earnings_per_day_adults = charge_per_adult * num_adults_per_day

    # L4
    total_earnings_per_day = earnings_per_day_adults + earnings_per_day_kids

    # L5
    days_per_week = 7 # WK
    total_earnings_per_week = total_earnings_per_day * days_per_week

    # FA
    answer = total_earnings_per_week
    return answer