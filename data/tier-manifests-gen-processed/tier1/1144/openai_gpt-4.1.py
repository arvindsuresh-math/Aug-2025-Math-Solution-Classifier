def solve():
    """Index: 1144.
    Returns: the combined age of Michael and his two brothers.
    """
    # L1
    younger_brother_age = 5 # younger brother is 5 years old
    third = 3 # a third of the age of the older brother
    oldest_brother_age = third * younger_brother_age

    # L2
    # 1 + (Michael's age - 1) * 2 = oldest_brother_age
    # (Michael's age - 1) * 2 = oldest_brother_age - 1
    # Michael's age - 1 = (oldest_brother_age - 1) / 2
    # Michael's age = ((oldest_brother_age - 1) / 2) + 1
    michaels_age = ((oldest_brother_age - 1) // 2) + 1

    # L3
    combined_age = younger_brother_age + oldest_brother_age + michaels_age

    # FA
    answer = combined_age
    return answer