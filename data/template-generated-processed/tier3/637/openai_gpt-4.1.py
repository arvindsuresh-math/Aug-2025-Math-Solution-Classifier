def solve():
    """Index: 637.
    Returns: Tony's age in 6 years.
    """
    # L1
    jacob_age = 24 # Jacob is 24 years now
    tony_age_divisor = 2 # Tony is half Jacob's age
    tony_age_now = jacob_age / tony_age_divisor

    # L2
    years_in_future = 6 # In 6 years
    tony_age_in_6_years = tony_age_now + years_in_future

    # FA
    answer = tony_age_in_6_years
    return answer