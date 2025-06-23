def solve(
    peppers_very_spicy_prev: int = 3, # 3 peppers for very spicy curries
    peppers_spicy_prev: int = 2, # 2 peppers for spicy curries
    peppers_mild_prev: int = 1, # 1 pepper for mild curries
    num_very_spicy_prev: int = 30, # 30 very spicy curries
    num_spicy_prev: int = 30, # 30 spicy curries
    num_mild_prev: int = 10, # 10 mild curries
    peppers_spicy_now: int = 2, # 2 peppers for spicy curries
    peppers_mild_now: int = 1, # 1 pepper for mild curries
    num_spicy_now: int = 15, # 15 spicy curries
    num_mild_now: int = 90 # 90 mild curries
):
    """Index: 2345.
    Returns: the number of fewer peppers the curry house now buys.
    """
    #: L1
    peppers_very_spicy_prev_total = peppers_very_spicy_prev * num_very_spicy_prev

    #: L2
    peppers_spicy_prev_total = peppers_spicy_prev * num_spicy_prev

    #: L3
    peppers_mild_prev_total = peppers_mild_prev * num_mild_prev

    #: L4
    total_peppers_prev = peppers_very_spicy_prev_total + peppers_spicy_prev_total + peppers_mild_prev_total

    #: L5
    peppers_spicy_now_total = peppers_spicy_now * num_spicy_now

    #: L6
    peppers_mild_now_total = peppers_mild_now * num_mild_now

    #: L7
    total_peppers_now = peppers_spicy_now_total + peppers_mild_now_total

    #: L8
    fewer_peppers_bought = total_peppers_prev - total_peppers_now

    answer = fewer_peppers_bought  # FINAL ANSWER
    return answer