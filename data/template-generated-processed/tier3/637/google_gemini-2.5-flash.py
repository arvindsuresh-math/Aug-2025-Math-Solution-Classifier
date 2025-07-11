def solve():
    """Index: 637.
    Returns: Tony's age in 6 years.
    """
    # L1
    jacob_age_now = 24 # Jacob is 24 years now
    half_divisor = 2 # half Jacob's age
    tony_age_now = jacob_age_now / half_divisor

    # L2
    years_from_now = 6 # In 6 years
    tony_age_future = tony_age_now + years_from_now

    # FA
    answer = tony_age_future
    return answer