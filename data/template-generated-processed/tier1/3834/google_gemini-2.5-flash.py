def solve():
    """Index: 3834.
    Returns: the total number of pitches Macy and Piper missed.
    """
    # L1
    macy_tokens = 11 # Macy used 11 tokens
    pitches_per_token = 15 # 15 pitches each
    macy_total_pitches = macy_tokens * pitches_per_token

    # L2
    piper_tokens = 17 # Piper used 17
    piper_total_pitches = piper_tokens * pitches_per_token

    # L3
    total_pitches_received = macy_total_pitches + piper_total_pitches

    # L4
    macy_hits = 50 # Macy hit the ball 50 times
    piper_hits = 55 # Piper hit the ball 55 times
    total_hits = macy_hits + piper_hits

    # L5
    total_misses = total_pitches_received - total_hits

    # FA
    answer = total_misses
    return answer