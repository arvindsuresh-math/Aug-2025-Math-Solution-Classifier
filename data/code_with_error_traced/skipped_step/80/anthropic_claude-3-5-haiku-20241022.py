def solve(
        initial_cans: int = 40,  # Jennifer purchased 40 cans of milk at the store
        mark_cans: int = 50,  # Mark purchased 50 cans
        jennifer_additional_cans_per_mark_cans: int = 6,  # Jennifer bought 6 additional cans for every 5 cans Mark bought
        mark_cans_ratio: int = 5  # Jennifer bought 6 additional cans for every 5 cans Mark bought
    ):
    """Index: 80.
    Returns: the total number of milk cans Jennifer brought home from the store.
    """

    #: L1

    #: L2
    additional_cans = mark_cans * jennifer_additional_cans_per_mark_cans # eval: 300 = 50 * 6

    #: L3
    total_cans = initial_cans + additional_cans # eval: 340 = 40 + 300

    #: FA
    answer = total_cans
    return answer # eval: return 340
