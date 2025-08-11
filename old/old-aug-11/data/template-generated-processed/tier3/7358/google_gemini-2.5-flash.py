def solve():
    """Index: 7358.
    Returns: the total number of miles Jack has driven.
    """
    # L1
    months_per_year = 12 # WK
    months_in_group = 4 # every four months
    four_month_groups_per_year = months_per_year / months_in_group

    # L2
    miles_per_four_months = 37000 # 37,000 miles every four months
    miles_per_year = miles_per_four_months * four_month_groups_per_year

    # L3
    years_driven = 9 # driving for the past 9 years
    total_miles_driven = miles_per_year * years_driven

    # FA
    answer = total_miles_driven
    return answer