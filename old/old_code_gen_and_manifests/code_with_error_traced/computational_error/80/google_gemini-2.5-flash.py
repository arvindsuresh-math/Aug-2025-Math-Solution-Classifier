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
    times_jennifer_added = 9.0 # eval: 9.0 = 9.0

    #: L2
    total_additional_cans_jennifer = times_jennifer_added * jennifer_additional_cans_per_ratio # eval: 54.0 = 9.0 * 6

    #: L3
    total_cans_jennifer_brought_home = jennifer_initial_cans + total_additional_cans_jennifer # eval: 94.0 = 40 + 54.0

    #: FA
    answer = total_cans_jennifer_brought_home
    return answer # eval: return 94.0
