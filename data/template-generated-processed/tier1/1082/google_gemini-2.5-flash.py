def solve():
    """Index: 1082.
    Returns: the total tonnes of maize Alfred has at the end of 2 years.
    """
    # L1
    maize_per_month = 1 # a tonne of maize each month
    months_in_year = 12 # WK
    maize_stored_in_1_year = months_in_year * maize_per_month

    # L2
    years_duration = 2 # for the next 2 years
    total_maize_stored_over_duration = months_in_year * years_duration

    # L3
    stolen_amount = 5 # 5 tonnes are stolen
    maize_after_stolen = total_maize_stored_over_duration - stolen_amount

    # L4
    donated_amount = 8 # 8 tonnes are given to him as a donation
    final_maize_amount = maize_after_stolen + donated_amount

    # FA
    answer = final_maize_amount
    return answer