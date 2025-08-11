def solve():
    """Index: 5617.
    Returns: the number of years Kayla needs to wait to reach the minimum driving age.
    """
    # L1
    kimiko_age = 26 # Kimiko who is 26 years old
    half_divisor = 2 # half the age
    kayla_current_age = kimiko_age / half_divisor

    # L2
    minimum_driving_age = 18 # minimum age of driving of her state, which is 18
    years_to_wait = minimum_driving_age - kayla_current_age

    # FA
    answer = years_to_wait
    return answer