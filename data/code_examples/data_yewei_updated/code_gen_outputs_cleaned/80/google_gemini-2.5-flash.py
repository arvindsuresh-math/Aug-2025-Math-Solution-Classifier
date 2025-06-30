def solve(
        initial_cans_jennifer: int = 40, # Jennifer purchased 40 cans of milk
        additional_cans_jennifer_per_block: int = 6, # 6 additional cans
        cans_mark_per_block: int = 5, # for every 5 cans Mark bought
        total_cans_mark_bought: int = 50 # Mark purchased 50 cans
    ):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """
    #: L1
    num_blocks_mark_bought = total_cans_mark_bought / cans_mark_per_block

    #: L2
    total_additional_cans_jennifer = num_blocks_mark_bought * additional_cans_jennifer_per_block

    #: L3
    total_cans_jennifer = initial_cans_jennifer + total_additional_cans_jennifer

    answer = total_cans_jennifer # FINAL ANSWER
    return answer