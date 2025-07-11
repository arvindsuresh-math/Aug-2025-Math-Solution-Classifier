def solve():
    """Index: 1889.
    Returns: the total money spent by the three friends over 4 years.
    """
    # L1
    trevor_spend = 80 # Trevor spends $80 every year
    trevor_more_than_reed = 20 # Trevor always spends $20 more than his friend Reed
    reed_spend = trevor_spend - trevor_more_than_reed

    # L2
    reed_times_quinn = 2 # Reed spends 2 times as much money as their friend Quinn
    quinn_spend = reed_spend / reed_times_quinn

    # L3
    total_spend_per_year = quinn_spend + reed_spend + trevor_spend

    # L4
    number_of_years = 4 # in 4 years
    total_spend_four_years = total_spend_per_year * number_of_years

    # FA
    answer = total_spend_four_years
    return answer