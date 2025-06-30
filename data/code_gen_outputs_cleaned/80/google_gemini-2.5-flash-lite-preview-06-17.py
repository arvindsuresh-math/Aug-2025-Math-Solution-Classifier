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
    times_jennifer_added_cans = cans_mark_bought / mark_cans_ratio

    #: L2
    additional_cans_jennifer = times_jennifer_added_cans * cans_jennifer_per_mark_cans

    #: L3
    total_cans_jennifer = initial_cans_jennifer + additional_cans_jennifer

    answer = total_cans_jennifer # FINAL ANSWER
    return answer