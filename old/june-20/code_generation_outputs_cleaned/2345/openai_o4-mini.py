def solve(
        peppers_per_very_spicy: int = 3, # 3 peppers for very spicy curries
        peppers_per_spicy: int = 2,      # 2 peppers for spicy curries
        peppers_per_mild: int = 1,       # 1 pepper for mild curries
        prev_very_spicy: int = 30,       # previously for 30 very spicy curries
        prev_spicy: int = 30,            # previously for 30 spicy curries
        prev_mild: int = 10,             # previously for 10 mild curries
        new_spicy: int = 15,             # now for 15 spicy curries
        new_mild: int = 90               # now for 90 mild curries
    ):
    """Index: 2345.
    Returns: how many fewer peppers the curry house now buys."""
    #: L1
    prev_peppers_very_spicy = peppers_per_very_spicy * prev_very_spicy
    #: L2
    prev_peppers_spicy = peppers_per_spicy * prev_spicy
    #: L3
    prev_peppers_mild = peppers_per_mild * prev_mild
    #: L4
    prev_total = prev_peppers_very_spicy + prev_peppers_spicy + prev_peppers_mild
    #: L5
    new_peppers_spicy = peppers_per_spicy * new_spicy
    #: L6
    new_peppers_mild = peppers_per_mild * new_mild
    #: L7
    new_total = new_peppers_spicy + new_peppers_mild
    #: L8
    answer = prev_total - new_total  # FINAL ANSWER
    return answer