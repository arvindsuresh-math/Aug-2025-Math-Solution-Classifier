def solve():
    """Index: 2635.
    Returns: the amount John saves per year by splitting the apartment compared to living alone.
    """
    # L1
    old_monthly_rent = 1200 # John's old apartment costs $1200 per month
    months_per_year = 12 # WK
    old_annual_rent = old_monthly_rent * months_per_year

    # L2
    price_increase_factor = 1.4 # 40% more expensive than John's old apartment
    new_monthly_rent = old_monthly_rent * price_increase_factor

    # L3
    num_people = 3 # John and his two brothers
    john_share_monthly = new_monthly_rent / num_people

    # L4
    john_share_annual = john_share_monthly * months_per_year

    # L5
    savings = old_annual_rent - john_share_annual

    # FA
    answer = savings
    return answer