def solve():
    """Index: 404.
    Returns: the number of bales of hay remaining.
    """
    # L1
    harvested_bales_last_year = 560 # harvested 560 bales of hay
    acres_last_year = 5 # from 5 acres of grass
    bales_per_acre_per_month = harvested_bales_last_year / acres_last_year

    # L2
    additional_acres = 7 # planted an additional 7 acres of grass
    total_acres_this_year = additional_acres + acres_last_year

    # L3
    expected_bales_per_month_this_year = total_acres_this_year * bales_per_acre_per_month

    # L4
    months_in_year = 12 # WK
    total_hay_production_this_year = expected_bales_per_month_this_year * months_in_year

    # L5
    days_september = 30 # WK
    days_october = 31 # WK
    days_november = 30 # WK
    days_december = 31 # WK
    total_feeding_days = days_september + days_october + days_november + days_december

    # L6
    bales_per_horse_per_day = 3 # each horse consumes 3 bales of hay a day
    num_horses = 9 # owns 9 horses
    daily_hay_consumption = bales_per_horse_per_day * num_horses

    # L7
    total_hay_consumed_by_horses = daily_hay_consumption * total_feeding_days

    # L8
    bales_remaining = total_hay_production_this_year - total_hay_consumed_by_horses

    # FA
    answer = bales_remaining
    return answer