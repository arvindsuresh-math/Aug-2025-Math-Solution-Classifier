def solve():
    """Index: 179.
    Returns: the number of stickers Colton has left.
    """
    # L1
    stickers_per_friend = 4 # gave 4 stickers each
    num_friends = 3 # to 3 friends
    stickers_given_to_friends = stickers_per_friend * num_friends

    # L2
    mandy_more_than_friends = 2 # 2 more than he gave his three friends total
    stickers_given_to_mandy = mandy_more_than_friends + stickers_given_to_friends

    # L3
    justin_less_than_mandy = 10 # 10 less than Mandy
    stickers_given_to_justin = stickers_given_to_mandy - justin_less_than_mandy

    # L4
    total_given = stickers_given_to_friends + stickers_given_to_mandy + stickers_given_to_justin

    # L5
    initial_stickers = 72 # Colton had 72 dolphin stickers
    stickers_left = initial_stickers - total_given

    # FA
    answer = stickers_left
    return answer