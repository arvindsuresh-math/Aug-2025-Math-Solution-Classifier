def solve():
    """Index: 514.
    Returns: the number of stickers Clara has left after giving stickers to the boy and her best friends.
    """
    # L2
    initial_stickers = 100 # Clara brings a package of 100 stickers to school
    stickers_given_to_boy = 10 # She gives 10 stickers to a boy she likes
    stickers_after_boy = initial_stickers - stickers_given_to_boy

    # L3
    friends_divisor = 2 # She gives half of the stickers which she has left
    stickers_given_to_friends = stickers_after_boy / friends_divisor

    # L4
    stickers_left = stickers_after_boy - stickers_given_to_friends

    # FA
    answer = stickers_left
    return answer