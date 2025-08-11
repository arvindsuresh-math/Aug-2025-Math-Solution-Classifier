def solve():
    """Index: 436.
    Returns: the total number of pens and pencils Catherine had left.
    """
    # L1
    pens_given_per_friend = 8 # gave eight pens ... to each friend
    num_friends = 7 # seven friends
    total_pens_given = pens_given_per_friend * num_friends

    # L2
    initial_pens = 60 # she had 60 pens
    pens_left = initial_pens - total_pens_given

    # L3
    pencils_given_per_friend = 6 # gave 6 pencils ... to each friend
    total_pencils_given = pencils_given_per_friend * num_friends

    # L4
    initial_pencils = 60 # had an equal number of pencils and pens
    pencils_left = initial_pencils - total_pencils_given

    # L5
    total_left = pens_left + pencils_left

    # FA
    answer = total_left
    return answer