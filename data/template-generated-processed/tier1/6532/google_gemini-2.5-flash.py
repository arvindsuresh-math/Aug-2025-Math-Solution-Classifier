def solve():
    """Index: 6532.
    Returns: the age of the younger son 30 years from now.
    """
    # L1
    elder_son_current_age = 40 # elder son is 40 years old now
    age_difference = 10 # difference in age ... is 10 years
    younger_son_current_age = elder_son_current_age - age_difference

    # L2
    years_from_now = 30 # 30 years from now
    younger_son_future_age = younger_son_current_age + years_from_now

    # FA
    answer = younger_son_future_age
    return answer