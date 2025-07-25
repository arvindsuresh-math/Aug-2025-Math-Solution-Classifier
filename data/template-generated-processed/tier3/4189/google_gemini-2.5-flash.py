def solve():
    """Index: 4189.
    Returns: 10 years less than their average age.
    """
    # L1
    luke_current_age = 20 # Luke is 20
    years_in_future = 8 # In eight years
    luke_age_in_eight_years = luke_current_age + years_in_future

    # L2
    bernard_age_multiplier = 3 # 3 times as old as Luke is now
    bernard_age_in_eight_years = bernard_age_multiplier * luke_current_age

    # L3
    bernard_current_age = bernard_age_in_eight_years - years_in_future

    # L4
    sum_current_ages = bernard_current_age + luke_current_age

    # L5
    number_of_people = 2 # WK
    average_age = sum_current_ages / number_of_people

    # L6
    less_than_average = 10 # 10 years less
    final_result = average_age - less_than_average

    # FA
    answer = final_result
    return answer