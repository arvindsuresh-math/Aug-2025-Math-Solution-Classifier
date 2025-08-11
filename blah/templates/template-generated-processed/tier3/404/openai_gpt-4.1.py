def solve():
    """Index: 404.
    Returns: the number of bales of hay the farmer has left by the end of December.
    """
    # L1
    last_year_bales = 560 # 560 bales of hay from 5 acres per month last year
    last_year_acres = 5 # 5 acres of grass per month last year
    bales_per_acre_per_month = last_year_bales / last_year_acres

    # L2
    additional_acres = 7 # planted an additional 7 acres
    total_acres = additional_acres + last_year_acres

    # L3
    bales_per_month = total_acres * bales_per_acre_per_month

    # L4
    months_in_year = 12 # WK
    total_bales_this_year = bales_per_month * months_in_year

    # L5
    sept_days = 30 # WK
    oct_days = 31 # WK
    nov_days = 30 # WK
    dec_days = 31 # WK
    feeding_days = sept_days + oct_days + nov_days + dec_days

    # L6
    bales_per_horse_per_day = 3 # each horse consumes 3 bales of hay a day
    num_horses = 9 # owns 9 horses
    daily_bales_consumed = bales_per_horse_per_day * num_horses

    # L7
    total_bales_consumed = daily_bales_consumed * feeding_days

    # L8
    bales_remaining = total_bales_this_year - total_bales_consumed

    # FA
    answer = bales_remaining
    return answer