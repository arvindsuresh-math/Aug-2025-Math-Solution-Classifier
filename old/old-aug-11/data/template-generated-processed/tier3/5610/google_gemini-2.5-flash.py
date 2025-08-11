def solve():
    """Index: 5610.
    Returns: the age of the youngest brother.
    """
    # L1
    rick_age = 15 # Rick has just celebrated his 15th birthday
    twice_age_multiplier = 2 # twice his age
    oldest_brother_age = rick_age * twice_age_multiplier

    # L2
    third_age_divisor = 3 # a third of the oldest brother’s age
    middle_brother_age = oldest_brother_age / third_age_divisor

    # L3
    half_age_divisor = 2 # half the middle brother’s age
    smallest_brother_age = middle_brother_age / half_age_divisor

    # L4
    younger_difference = 2 # 2 years younger than the smallest brother
    youngest_brother_age = smallest_brother_age - younger_difference

    # FA
    answer = youngest_brother_age
    return answer