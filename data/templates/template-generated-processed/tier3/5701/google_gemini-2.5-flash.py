def solve():
    """Index: 5701.
    Returns: Simon's age.
    """
    # L1
    alvin_age = 30 # Alvin is 30 years old
    half_age_divisor = 2 # 1/2 the age of Alvin
    half_alvin_age = alvin_age / half_age_divisor

    # L2
    years_away = 5 # 5 years away from being 1/2 the age of Alvin
    simon_age = half_alvin_age - years_away

    # FA
    answer = simon_age
    return answer