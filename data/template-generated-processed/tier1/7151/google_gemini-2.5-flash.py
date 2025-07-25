def solve():
    """Index: 7151.
    Returns: the total amount Kate paid for all visits to the Art-museum after 3 years.
    """
    # L1
    entrance_fee_initial = 5 # The entrance fee is $5
    months_per_year = 12 # WK
    cost_first_year = entrance_fee_initial * months_per_year

    # L2
    total_years = 3 # after 3 years of visiting
    first_period_years = 1 # After 1 year
    remaining_years = total_years - first_period_years

    # L3
    visits_per_year_later = 4 # visit the museum only 4 times a year
    total_visits_later = remaining_years * visits_per_year_later

    # L4
    entrance_fee_later = 7 # ticket price increased to $7
    cost_later_years = entrance_fee_later * total_visits_later

    # L5
    total_cost = cost_later_years + cost_first_year

    # FA
    answer = total_cost
    return answer