def solve():
    """Index: 2989.
    Returns: the number of stamps Tonya has left.
    """
    # L1
    jimmy_matchbooks = 5 # Jimmy has 5 matchbooks
    matches_per_matchbook = 24 # Each matchbook contains 24 matches
    jimmy_total_matches = jimmy_matchbooks * matches_per_matchbook

    # L2
    matches_per_stamp = 12 # one stamp is worth 12 matches
    stamps_jimmy_gets = jimmy_total_matches / matches_per_stamp

    # L3
    tonya_initial_stamps = 13 # Tonya arrives with 13 stamps
    tonya_stamps_left = tonya_initial_stamps - stamps_jimmy_gets

    # FA
    answer = tonya_stamps_left
    return answer