def solve():
    """Index: 2143.
    Returns: the distance, in feet, that the fourth competitor jumped.
    """
    # L1
    first_jump = 22 # The first competitor jumped a distance of 22 feet
    second_more_than_first = 1 # one foot farther than the first competitor
    second_jump = first_jump + second_more_than_first

    # L2
    third_shorter_than_second = 2 # two feet shorter than the third competitor (should be 'second competitor' by context)
    third_jump = second_jump - third_shorter_than_second

    # L3
    fourth_more_than_third = 3 # 3 feet further than the third competitor
    fourth_jump = third_jump + fourth_more_than_third

    # FA
    answer = fourth_jump
    return answer