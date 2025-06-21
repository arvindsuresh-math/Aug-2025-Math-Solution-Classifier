def solve(
    peppers_per_very_spicy: int = 3, # needs 3 peppers for very spicy curries
    peppers_per_spicy: int = 2, # 2 peppers for spicy curries
    peppers_per_mild: int = 1, # only 1 pepper for mild curries
    prev_num_very_spicy: int = 30, # Previously, the curry house was buying enough peppers for 30 very spicy curries
    prev_num_spicy: int = 30, # 30 spicy curries
    prev_num_mild: int = 10, # and 10 mild curries
    curr_num_spicy: int = 15, # They now buy enough peppers for 15 spicy curries
    curr_num_mild: int = 90 # and 90 mild curries
):
    """Index: 2345.
    Returns: the number of fewer peppers the curry house now buys compared to previously.
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
    curr_peppers_spicy = peppers_per_spicy * curr_num_spicy

    #: L6
    curr_peppers_mild = peppers_per_mild * curr_num_mild

    #: L7
    total_curr_peppers = curr_peppers_spicy + curr_peppers_mild

    #: L8
    peppers_difference = total_prev_peppers - total_curr_peppers

    answer = peppers_difference # FINAL ANSWER
    return answer