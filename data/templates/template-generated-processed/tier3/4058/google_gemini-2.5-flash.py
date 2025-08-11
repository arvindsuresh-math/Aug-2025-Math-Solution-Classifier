def solve():
    """Index: 4058.
    Returns: the age of Tom's dog in six years.
    """
    # L1
    brother_future_age = 30 # will be 30 years
    years_in_future = 6 # in 6 years
    brother_current_age = brother_future_age - years_in_future

    # L2
    brother_age_multiplier = 4 # 4 times as old
    dog_current_age = brother_current_age / brother_age_multiplier

    # L3
    dog_future_age = dog_current_age + years_in_future

    # FA
    answer = dog_future_age
    return answer