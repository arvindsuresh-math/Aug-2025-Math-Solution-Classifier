def solve():
    """Index: 869.
    Returns: the number of stickers Paige will have left.
    """
    # L1
    space_stickers = 100 # a sheet of 100 space stickers
    num_friends = 3 # 3 of her friends
    space_stickers_per_friend = space_stickers // num_friends
    space_stickers_remainder = space_stickers % num_friends

    # L2
    cat_stickers = 50 # a sheet of 50 cat stickers
    cat_stickers_per_friend = cat_stickers // num_friends
    cat_stickers_remainder = cat_stickers % num_friends

    # L3
    total_stickers_left = space_stickers_remainder + cat_stickers_remainder

    # FA
    answer = total_stickers_left
    return answer