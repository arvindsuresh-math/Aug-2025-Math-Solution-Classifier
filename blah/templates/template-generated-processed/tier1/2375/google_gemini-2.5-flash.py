def solve():
    """Index: 2375.
    Returns: the total number of envelopes Wyatt has.
    """
    # L1
    blue_envelopes = 10 # 10 blue envelopes
    fewer_yellow_envelopes = 4 # 4 fewer yellow envelopes than blue envelopes
    yellow_envelopes = blue_envelopes - fewer_yellow_envelopes

    # L2
    total_envelopes = blue_envelopes + yellow_envelopes

    # FA
    answer = total_envelopes
    return answer