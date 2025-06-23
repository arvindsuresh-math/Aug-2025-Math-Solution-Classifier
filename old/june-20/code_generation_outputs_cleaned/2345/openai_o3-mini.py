def solve(
    peppers_per_very_spicy: int = 3,  # "needs 3 peppers for very spicy curries"
    peppers_per_spicy: int = 2,       # "2 peppers for spicy curries"
    peppers_per_mild: int = 1,        # "only 1 pepper for mild curries"
    very_spicy_count_prev: int = 30,  # "Previously, the curry house was buying enough peppers for 30 very spicy curries"
    spicy_count_prev: int = 30,       # "30 spicy curries"
    mild_count_prev: int = 10,        # "10 mild curries"
    spicy_count_new: int = 15,        # "now buy enough peppers for 15 spicy curries"
    mild_count_new: int = 90          # "and 90 mild curries"
):
    """Index: 2345.
    Returns: the difference in the number of peppers purchased previously and now.
    """
    #: L1
    previous_peppers_very_spicy = peppers_per_very_spicy * very_spicy_count_prev

    #: L2
    previous_peppers_spicy = peppers_per_spicy * spicy_count_prev

    #: L3
    previous_peppers_mild = peppers_per_mild * mild_count_prev

    #: L4
    total_previous_peppers = previous_peppers_very_spicy + previous_peppers_spicy + previous_peppers_mild

    #: L5
    new_peppers_spicy = peppers_per_spicy * spicy_count_new

    #: L6
    new_peppers_mild = peppers_per_mild * mild_count_new

    #: L7
    total_new_peppers = new_peppers_spicy + new_peppers_mild

    #: L8
    pepper_difference = total_previous_peppers - total_new_peppers

    answer = pepper_difference  # FINAL ANSWER
    return answer