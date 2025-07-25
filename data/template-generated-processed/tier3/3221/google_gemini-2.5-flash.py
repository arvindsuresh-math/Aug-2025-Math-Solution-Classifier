def solve():
    """Index: 3221.
    Returns: the age of the oldest sibling.
    """
    # L1
    kay_age = 32 # Kay is 32 years old

    # L2
    half_divisor = 2 # half Kay's age
    less_than_value = 5 # 5 less than half Kay's age
    youngest_sibling_age = kay_age / half_divisor - less_than_value

    # L3
    multiplier_oldest = 4 # four times as old as the youngest sibling
    oldest_sibling_age = youngest_sibling_age * multiplier_oldest

    # FA
    answer = oldest_sibling_age
    return answer