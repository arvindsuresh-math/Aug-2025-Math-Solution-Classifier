def solve():
    """Index: 6264.
    Returns: the number of girls at the camp.
    """
    # L1
    total_people = 133 # 133 people at a camp
    boy_girl_difference = 33 # 33 more boys than girls
    people_if_equal = total_people - boy_girl_difference

    # L2
    equal_parts_divisor = 2 # WK
    number_of_girls = people_if_equal / equal_parts_divisor

    # FA
    answer = number_of_girls
    return answer