def solve():
    """Index: 1477.
    Returns: the amount of deer Jack keeps in pounds per year.
    """
    # L1
    months_per_year = 12 # WK
    hunting_season_quarter = 4 # 1 quarter of the year
    hunting_season_months = months_per_year / hunting_season_quarter

    # L2
    hunting_frequency_per_month = 6 # Jack goes hunting 6 times a month
    total_hunts_per_year = hunting_season_months * hunting_frequency_per_month

    # L3
    deers_per_hunt = 2 # catches 2 deers each time he goes hunting
    total_deers_per_year = total_hunts_per_year * deers_per_hunt

    # L4
    deer_weight_per_deer = 600 # weigh 600 pounds each
    total_pounds_caught_per_year = total_deers_per_year * deer_weight_per_deer

    # L5
    keep_fraction_denominator = 2 # keeps half the weight of deer
    pounds_kept_per_year = total_pounds_caught_per_year / keep_fraction_denominator

    # FA
    answer = pounds_kept_per_year
    return answer