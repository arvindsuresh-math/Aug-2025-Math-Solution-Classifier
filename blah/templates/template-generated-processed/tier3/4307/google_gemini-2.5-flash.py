def solve():
    """Index: 4307.
    Returns: the amount of money Mr. Maximilian receives in that year.
    """
    # L1
    total_units = 100 # The number of units in the building is 100
    occupied_numerator = 3 # 3/4 occupied
    occupied_denominator = 4 # 3/4 occupied
    occupied_units = occupied_numerator / occupied_denominator * total_units

    # L2
    rent_per_unit_per_month = 400 # each resident of the building pays a rent of $400
    monthly_revenue = occupied_units * rent_per_unit_per_month

    # L3
    months_per_year = 12 # WK
    annual_revenue = monthly_revenue * months_per_year

    # FA
    answer = annual_revenue
    return answer