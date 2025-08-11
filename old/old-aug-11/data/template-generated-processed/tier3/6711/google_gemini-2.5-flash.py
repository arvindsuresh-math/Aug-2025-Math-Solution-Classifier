def solve():
    """Index: 6711.
    Returns: Diaz's age 20 years from now.
    """
    # L1
    sierra_current_age = 30 # Sierra is currently 30 years old
    multiplier_for_age = 10 # 10 times Diaz's age is 20 more than 10 times Sierra's age
    ten_times_sierra_age = sierra_current_age * multiplier_for_age

    # L2
    twenty_more = 20 # 20 more than 10 times Sierra's age
    twenty_more_than_ten_times_sierra_age = ten_times_sierra_age + twenty_more

    # L3
    forty_less = 40 # 40 less than 10 times Diaz's age
    ten_times_diaz_age = twenty_more_than_ten_times_sierra_age + forty_less

    # L4
    diaz_current_age = ten_times_diaz_age / multiplier_for_age

    # L5
    years_from_now = 20 # 20 years from now
    diaz_age_future = years_from_now + diaz_current_age

    # FA
    answer = diaz_age_future
    return answer