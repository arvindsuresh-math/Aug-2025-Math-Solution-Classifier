def solve():
    """Index: 1208.
    Returns: the sum of the age of the babies in five years.
    """
    # L1
    lioness_age = 12 # The lioness is 12 years old
    half_age_divisor = 2 # half her age
    hyena_age = lioness_age / half_age_divisor

    # L2
    lioness_baby_age = lioness_age / half_age_divisor

    # L3
    years_from_now = 5 # in five years
    lioness_baby_age_future = lioness_baby_age + years_from_now

    # L4
    hyena_baby_age = hyena_age / half_age_divisor

    # L5
    hyena_baby_age_future = hyena_baby_age + years_from_now

    # L6
    total_babies_age_future = hyena_baby_age_future + lioness_baby_age_future

    # FA
    answer = total_babies_age_future
    return answer