def solve():
    """Index: 5111.
    Returns: the total of the ages of the three siblings 10 years from now.
    """
    # L1
    elder_child_current_age = 20 # eldest child is 20 years old now
    years_from_now = 10 # 10 years from now
    elder_child_age_future = elder_child_current_age + years_from_now

    # L2
    age_difference = 5 # born 5 years apart
    second_born_current_age = elder_child_current_age - age_difference

    # L3
    second_born_age_future = second_born_current_age + years_from_now

    # L4
    total_age_first_two_future = second_born_age_future + elder_child_age_future

    # L5
    third_born_current_age = second_born_current_age - age_difference

    # L6
    third_born_age_future = third_born_current_age + years_from_now

    # L7
    total_age_three_siblings_future = total_age_first_two_future + third_born_age_future

    # FA
    answer = total_age_three_siblings_future
    return answer