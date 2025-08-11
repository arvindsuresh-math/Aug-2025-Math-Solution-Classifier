def solve():
    """Index: 1144.
    Returns: the combined age of Michael and his two brothers.
    """
    # L1
    younger_brother_age = 5 # His younger brother is 5 years old
    older_brother_multiplier = 3 # a third of the age of the older brother
    oldest_brother_age = older_brother_multiplier * younger_brother_age

    # L2
    age_difference_older = 1 # 1 year older
    age_difference_younger = 1 # a year younger
    age_multiplier_twice = 2 # twice Michael's age
    michael_age = (oldest_brother_age - age_difference_older) / age_multiplier_twice + age_difference_younger

    # L3
    combined_age = younger_brother_age + oldest_brother_age + michael_age

    # FA
    answer = combined_age
    return answer