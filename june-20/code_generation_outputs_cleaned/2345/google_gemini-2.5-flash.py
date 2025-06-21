def solve(
        peppers_per_very_spicy: int = 3, # 3 peppers for very spicy curries
        peppers_per_spicy: int = 2, # 2 peppers for spicy curries
        peppers_per_mild: int = 1, # 1 pepper for mild curries
        prev_num_very_spicy: int = 30, # 30 very spicy curries
        prev_num_spicy: int = 30, # 30 spicy curries
        prev_num_mild: int = 10, # 10 mild curries
        new_num_spicy: int = 15, # 15 spicy curries
        new_num_mild: int = 90 # 90 mild curries
    ):
    """Index: 2345.
    Returns: the reduction in the number of peppers bought by the curry house.
    """
    #: L1
    prev_peppers_very_spicy = peppers_per_very_spicy * prev_num_very_spicy

    #: L2
    prev_peppers_spicy = peppers_per_spicy * prev_num_spicy

    #: L3
    prev_peppers_mild = peppers_per_mild * prev_num_mild

    #: L4
    total_prev_peppers = prev_peppers_very_spicy + prev_peppers_spicy + prev_peppers_mild

    #: L5
    new_peppers_spicy = peppers_per_spicy * new_num_spicy

    #: L6
    new_peppers_mild = peppers_per_mild * new_num_mild

    #: L7
    total_new_peppers = new_peppers_spicy + new_peppers_mild

    #: L8
    fewer_peppers_bought = total_prev_peppers - total_new_peppers

    answer = fewer_peppers_bought # FINAL ANSWER
    return answer