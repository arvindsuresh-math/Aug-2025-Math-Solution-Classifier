def solve(
    peppers_per_very_spicy: int = 3, # needs 3 peppers for very spicy curries
    peppers_per_spicy: int = 2, # needs 2 peppers for spicy curries
    peppers_per_mild: int = 1, # needs 1 pepper for mild curries
    prev_very_spicy: int = 30, # previously buying for 30 very spicy curries
    prev_spicy: int = 30, # previously buying for 30 spicy curries
    prev_mild: int = 10, # previously buying for 10 mild curries
    now_spicy: int = 15, # now buys for 15 spicy curries
    now_mild: int = 90 # now buys for 90 mild curries
):
    """Index: 2345.
    Returns: the number of peppers fewer that the curry house now buys compared to before.
    """
    #: L1
    prev_peppers_very_spicy = peppers_per_very_spicy * prev_very_spicy

    #: L2
    prev_peppers_spicy = peppers_per_spicy * prev_spicy

    #: L3
    prev_peppers_mild = peppers_per_mild * prev_mild

    #: L4
    prev_total_peppers = prev_peppers_very_spicy + prev_peppers_spicy + prev_peppers_mild

    #: L5
    now_peppers_spicy = peppers_per_spicy * now_spicy

    #: L6
    now_peppers_mild = peppers_per_mild * now_mild

    #: L7
    now_total_peppers = now_peppers_spicy + now_peppers_mild

    #: L8
    answer = prev_total_peppers - now_total_peppers # FINAL ANSWER
    return answer