def solve():
    """Index: 7362.
    Returns: the age of the other two boys.
    """
    # L1
    total_sum_ages = 29 # The sum of the ages of three boys is 29
    third_boy_age = 11 # the third boy is 11 years old
    sum_of_first_two_ages = total_sum_ages - third_boy_age

    # L2
    num_boys_same_age = 2 # two of the boys are the same age
    age_of_each_boy = sum_of_first_two_ages / num_boys_same_age

    # FA
    answer = age_of_each_boy
    return answer