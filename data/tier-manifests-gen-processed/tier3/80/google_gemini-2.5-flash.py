def solve():
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home.
    """
    # L1
    mark_cans_bought = 50 # Mark purchased 50 cans
    cans_per_block = 5 # for every 5 cans Mark bought
    times_jennifer_added = mark_cans_bought / cans_per_block

    # L2
    additional_cans_per_block = 6 # 6 additional cans
    total_additional_cans = times_jennifer_added * additional_cans_per_block

    # L3
    initial_jennifer_cans = 40 # Jennifer purchased 40 cans of milk
    total_jennifer_cans = initial_jennifer_cans + total_additional_cans

    # FA
    answer = total_jennifer_cans
    return answer