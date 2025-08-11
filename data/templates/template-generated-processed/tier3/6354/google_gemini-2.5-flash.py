def solve():
    """Index: 6354.
    Returns: the brother's age in 5 years.
    """
    # L1
    nick_age = 13 # Nick is 13 years old
    sister_age_difference = 6 # His sister is 6 years older
    sister_age = nick_age + sister_age_difference

    # L2
    combined_age = sister_age + nick_age

    # L3
    brother_age_divisor = 2 # half their combined age
    brother_age = combined_age / brother_age_divisor

    # L4
    years_in_future = 5 # In 5 years
    brother_age_in_future = brother_age + years_in_future

    # FA
    answer = brother_age_in_future
    return answer