def solve(
    initial_cans_jennifer: int = 40, # Jennifer purchased 40 cans of milk
    cans_jennifer_per_mark_cans: int = 6, # Jennifer bought 6 additional cans
    mark_cans_ratio: int = 5, # for every 5 cans Mark bought
    cans_mark_bought: int = 50 # If Mark purchased 50 cans
):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """

    #: L1
    times_jennifer_added_cans = cans_mark_bought / mark_cans_ratio # eval: 10.0 = 50 / 5

    #: L2

    #: L3
    total_cans_jennifer = initial_cans_jennifer + cans_mark_bought # eval: 90 = 40 + 50

    #: FA
    answer = total_cans_jennifer
    return answer # eval: return 90
