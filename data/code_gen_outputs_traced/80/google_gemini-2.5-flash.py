def solve(
        jennifer_initial_cans: int = 40, # Jennifer purchased 40 cans of milk
        jennifer_additional_cans_per_ratio: int = 6, # Jennifer bought 6 additional cans
        mark_cans_per_ratio: int = 5, # for every 5 cans Mark bought
        mark_total_cans: int = 50 # If Mark purchased 50 cans
    ):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """
    #: L1
    times_jennifer_added = mark_total_cans / mark_cans_per_ratio # eval: 10.0 = 50 / 5
    #: L2
    total_additional_cans_jennifer = times_jennifer_added * jennifer_additional_cans_per_ratio # eval: 60.0 = 10.0 * 6
    #: L3
    total_cans_jennifer_brought_home = jennifer_initial_cans + total_additional_cans_jennifer # eval: 100.0 = 40 + 60.0
    answer = total_cans_jennifer_brought_home # FINAL ANSWER # eval: 100.0 = 100.0 # FINAL ANSWER
    return answer # eval: return 100.0