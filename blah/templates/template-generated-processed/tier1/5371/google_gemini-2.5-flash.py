def solve():
    """Index: 5371.
    Returns: the number of additional apples Martha needs to give away.
    """
    # L1
    jane_apples = 5 # Jane got 5 apples from her
    james_more_than_jane = 2 # James got 2 more than Jane
    james_apples = jane_apples + james_more_than_jane

    # L2
    initial_apples = 20 # Martha has 20 apples
    apples_remaining_after_giving = initial_apples - jane_apples - james_apples

    # L3
    target_remaining_apples = 4 # to be left with only 4 of them
    apples_to_give_away_more = apples_remaining_after_giving - target_remaining_apples

    # FA
    answer = apples_to_give_away_more
    return answer