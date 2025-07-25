def solve():
    """Index: 2461.
    Returns: the worth of the car after 6 years.
    """
    # L1
    annual_depreciation = 1000 # goes down in value by $1000 a year
    years = 6 # after 6 years
    total_depreciation = annual_depreciation * years

    # L2
    initial_value = 20000 # bought it for $20,000
    current_value = initial_value - total_depreciation

    # FA
    answer = current_value
    return answer