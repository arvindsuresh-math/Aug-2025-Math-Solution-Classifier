def solve():
    """Index: 2461.
    Returns: the value of Tim's car after 6 years.
    """
    # L1
    depreciation_per_year = 1000 # goes down in value by $1000 a year
    years = 6 # after 6 years
    total_depreciation = depreciation_per_year * years

    # L2
    initial_value = 20000 # bought it for $20,000
    car_value_after_years = initial_value - total_depreciation

    # FA
    answer = car_value_after_years
    return answer