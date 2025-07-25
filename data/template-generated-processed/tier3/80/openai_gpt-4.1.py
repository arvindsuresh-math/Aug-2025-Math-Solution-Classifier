def solve():
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """
    # L1
    mark_cans = 50 # Mark purchased 50 cans
    mark_per_jennifer = 5 # for every 5 cans Mark bought
    times_jennifer_added = mark_cans / mark_per_jennifer

    # L2
    jennifer_added_per_time = 6 # Jennifer bought 6 additional cans
    total_additional_cans = times_jennifer_added * jennifer_added_per_time

    # L3
    initial_jennifer_cans = 40 # Jennifer purchased 40 cans of milk at the store
    total_jennifer_cans = initial_jennifer_cans + total_additional_cans

    # FA
    answer = total_jennifer_cans
    return answer