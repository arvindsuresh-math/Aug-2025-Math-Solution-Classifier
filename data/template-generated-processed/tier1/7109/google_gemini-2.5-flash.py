def solve():
    """Index: 7109.
    Returns: the number of cans of silly string Michelle had to start with.
    """
    # L1
    roger_cans_after_giving = 4 # he now has 4 for himself
    roger_gave_to_brothers = 2 # give 2 of his cans to his brothers
    roger_original_cans = roger_cans_after_giving + roger_gave_to_brothers

    # L2
    num_friends = 3 # 3 of his friends
    friends_total_cans = num_friends * roger_original_cans

    # L3
    michelle_start_cans = roger_original_cans + friends_total_cans

    # FA
    answer = michelle_start_cans
    return answer