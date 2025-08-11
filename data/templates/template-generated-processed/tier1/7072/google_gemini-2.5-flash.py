def solve():
    """Index: 7072.
    Returns: the sum of Divya and Nacho's current ages.
    """
    # L1
    divya_current_age = 5 # Divya is currently 5 years old
    years_in_future = 5 # In 5 years
    divya_age_in_future = divya_current_age + years_in_future

    # L2
    nacho_age_multiplier = 3 # three times older
    nacho_age_difference_in_future = nacho_age_multiplier * divya_age_in_future

    # L3
    nacho_total_age_in_future = nacho_age_difference_in_future + divya_age_in_future

    # L4
    nacho_current_age = nacho_total_age_in_future - years_in_future

    # L5
    sum_of_current_ages = nacho_current_age + divya_current_age

    # FA
    answer = sum_of_current_ages
    return answer