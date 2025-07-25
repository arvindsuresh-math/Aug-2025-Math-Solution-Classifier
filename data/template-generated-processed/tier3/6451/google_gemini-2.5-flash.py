def solve():
    """Index: 6451.
    Returns: the total annual cost of oil changes.
    """
    # L1
    oil_change_interval_miles = 3000 # every 3000 miles
    miles_per_month = 1000 # drives 1000 miles a month
    oil_change_interval_months = oil_change_interval_miles / miles_per_month

    # L2
    months_per_year = 12 # WK
    total_oil_changes_per_year = months_per_year / oil_change_interval_months

    # L3
    free_oil_changes_per_year = 1 # 1 free oil change a year
    paid_oil_changes_per_year = total_oil_changes_per_year - free_oil_changes_per_year

    # L4
    cost_per_oil_change = 50 # an oil change costs $50
    total_annual_cost = paid_oil_changes_per_year * cost_per_oil_change

    # FA
    answer = total_annual_cost
    return answer