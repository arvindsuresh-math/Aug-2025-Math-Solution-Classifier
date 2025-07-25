def solve():
    """Index: 4510.
    Returns: the age of Mark and John's parents when Mark was born.
    """
    # L1
    mark_age = 18 # Mark is 18 years old
    john_younger_than_mark = 10 # John, who is 10 years younger
    john_age = mark_age - john_younger_than_mark

    # L2
    parents_age_multiplier = 5 # parents are currently 5 times older than John
    parents_current_age = john_age * parents_age_multiplier

    # L3
    parents_age_at_mark_birth = parents_current_age - mark_age

    # FA
    answer = parents_age_at_mark_birth
    return answer