def solve():
    """Index: 436.
    Returns: the total number of pens and pencils Catherine had left.
    """
    # L1
    pens_per_friend = 8 # gave eight pens
    num_friends = 7 # seven friends
    pens_given_away = pens_per_friend * num_friends

    # L2
    initial_pens = 60 # 60 pens
    pens_remaining = initial_pens - pens_given_away

    # L3
    pencils_per_friend = 6 # 6 pencils
    pencils_given_away = pencils_per_friend * num_friends

    # L4
    initial_pencils = 60 # equal number of pencils and pens (and she had 60 pens)
    pencils_remaining = initial_pencils - pencils_given_away

    # L5
    total_remaining = pens_remaining + pencils_remaining

    # FA
    answer = total_remaining
    return answer