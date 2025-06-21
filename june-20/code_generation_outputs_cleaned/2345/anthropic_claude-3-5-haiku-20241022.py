def solve(
        peppers_very_spicy: int = 3,  # 3 peppers for very spicy curries
        peppers_spicy: int = 2,  # 2 peppers for spicy curries
        peppers_mild: int = 1,  # 1 pepper for mild curries
        prev_very_spicy_curries: int = 30,  # previously 30 very spicy curries
        prev_spicy_curries: int = 30,  # previously 30 spicy curries
        prev_mild_curries: int = 10,  # previously 10 mild curries
        current_spicy_curries: int = 15,  # now 15 spicy curries
        current_mild_curries: int = 90  # now 90 mild curries
    ):
    """Index: 2345.
    Returns: the number of fewer peppers the curry house now buys.
    """
    #: L1
    prev_very_spicy_peppers = peppers_very_spicy * prev_very_spicy_curries

    #: L2
    prev_spicy_peppers = peppers_spicy * prev_spicy_curries

    #: L3
    prev_mild_peppers = peppers_mild * prev_mild_curries

    #: L4
    prev_total_peppers = prev_very_spicy_peppers + prev_spicy_peppers + prev_mild_peppers

    #: L5
    current_spicy_peppers = peppers_spicy * current_spicy_curries

    #: L6
    current_mild_peppers = peppers_mild * current_mild_curries

    #: L7
    current_total_peppers = current_spicy_peppers + current_mild_peppers

    #: L8
    peppers_reduction = prev_total_peppers - current_total_peppers

    answer = peppers_reduction  # FINAL ANSWER
    return answer