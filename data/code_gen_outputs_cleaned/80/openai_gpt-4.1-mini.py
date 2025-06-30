def solve(
    initial_cans_jennifer: int = 40,  # Jennifer purchased 40 cans of milk
    additional_cans_per_5_mark: int = 6,  # Jennifer bought 6 additional cans for every 5 cans Mark bought
    cans_mark_bought: int = 50  # Mark purchased 50 cans
):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """
    #: L1
    times_additional_cans = cans_mark_bought / 5

    #: L2
    total_additional_cans = times_additional_cans * additional_cans_per_5_mark

    #: L3
    total_cans_jennifer = initial_cans_jennifer + total_additional_cans

    answer = total_cans_jennifer  # FINAL ANSWER
    return answer