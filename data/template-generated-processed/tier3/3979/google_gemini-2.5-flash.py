def solve():
    """Index: 3979.
    Returns: the total gallons of diesel fuel Mr. Alvarez uses in two weeks.
    """
    # L1
    weekly_spend = 36 # $36 on diesel fuel each week
    cost_per_gallon = 3 # $3 per gallon
    gallons_per_week = weekly_spend / cost_per_gallon

    # L2
    number_of_weeks = 2 # two weeks
    total_gallons = gallons_per_week * number_of_weeks

    # FA
    answer = total_gallons
    return answer