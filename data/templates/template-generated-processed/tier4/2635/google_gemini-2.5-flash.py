def solve():
    """Index: 2635.
    Returns: the amount John saves per year by splitting the apartment.
    """
    # L1
    old_apartment_monthly_cost = 1200 # $1200 per month
    months_per_year = 12 # WK
    old_apartment_yearly_cost = old_apartment_monthly_cost * months_per_year

    # L2
    new_apartment_cost_factor = 1.4 # 40% more expensive
    new_apartment_monthly_total_cost = old_apartment_monthly_cost * new_apartment_cost_factor

    # L3
    num_people_splitting = 3 # John and his two brothers
    johns_new_apartment_monthly_cost = new_apartment_monthly_total_cost / num_people_splitting

    # L4
    johns_new_apartment_yearly_cost = johns_new_apartment_monthly_cost * months_per_year

    # L5
    yearly_savings = old_apartment_yearly_cost - johns_new_apartment_yearly_cost

    # FA
    answer = yearly_savings
    return answer