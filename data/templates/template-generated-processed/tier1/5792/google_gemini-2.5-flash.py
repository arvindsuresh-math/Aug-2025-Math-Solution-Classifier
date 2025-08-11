def solve():
    """Index: 5792.
    Returns: the number of envelopes Cindy has left.
    """
    # L1
    envelopes_per_friend = 3 # 3 envelopes to each of her 5 friends
    num_friends = 5 # 5 friends
    envelopes_given = envelopes_per_friend * num_friends

    # L2
    initial_envelopes = 37 # Cindy has 37 envelopes
    envelopes_left = initial_envelopes - envelopes_given

    # FA
    answer = envelopes_left
    return answer