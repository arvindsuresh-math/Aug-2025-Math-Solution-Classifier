def solve():
    """Index: 514.
    Returns: the number of stickers Clara has left.
    """
    # L2
    total_stickers = 100 # a package of 100 stickers
    stickers_given_to_boy = 10 # gives 10 stickers to a boy she likes
    stickers_after_boy = total_stickers - stickers_given_to_boy

    # L3
    friends_share_divisor = 2 # gives half of the stickers
    stickers_given_to_friends = stickers_after_boy / friends_share_divisor

    # L4
    stickers_left = stickers_after_boy - stickers_given_to_friends

    # FA
    answer = stickers_left
    return answer