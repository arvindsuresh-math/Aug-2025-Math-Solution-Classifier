def solve():
    """Index: 2345.
    Returns: how many fewer peppers the curry house now buys.
    """
    # L1
    peppers_per_very_spicy = 3 # needs 3 peppers for very spicy curries
    num_very_spicy_prev = 30 # 30 very spicy curries
    peppers_very_spicy_prev = peppers_per_very_spicy * num_very_spicy_prev

    # L2
    peppers_per_spicy = 2 # needs 2 peppers for spicy curries
    num_spicy_prev = 30 # 30 spicy curries
    peppers_spicy_prev = peppers_per_spicy * num_spicy_prev

    # L3
    peppers_per_mild = 1 # needs 1 pepper for mild curries
    num_mild_prev = 10 # 10 mild curries
    peppers_mild_prev = peppers_per_mild * num_mild_prev

    # L4
    total_peppers_prev = peppers_very_spicy_prev + peppers_spicy_prev + peppers_mild_prev

    # L5
    num_spicy_now = 15 # 15 spicy curries
    peppers_spicy_now = peppers_per_spicy * num_spicy_now

    # L6
    num_mild_now = 90 # 90 mild curries
    peppers_mild_now = peppers_per_mild * num_mild_now

    # L7
    total_peppers_now = peppers_spicy_now + peppers_mild_now

    # L8
    peppers_difference = total_peppers_prev - total_peppers_now

    # FA
    answer = peppers_difference
    return answer