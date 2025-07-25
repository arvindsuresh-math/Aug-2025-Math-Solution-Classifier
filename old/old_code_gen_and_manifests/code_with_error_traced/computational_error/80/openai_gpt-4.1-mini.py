def solve(
    initial_cans_jennifer: int = 40,  # Jennifer purchased 40 cans of milk
    additional_cans_per_5_mark: int = 6,  # Jennifer bought 6 additional cans for every 5 cans Mark bought
    cans_mark_bought: int = 50  # Mark purchased 50 cans
):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home from the store.
    """

    #: L1
    times_additional_cans = 9.0 # eval: 9.0 = 9.0

    #: L2
    total_additional_cans = times_additional_cans * additional_cans_per_5_mark # eval: 54.0 = 9.0 * 6

    #: L3
    total_cans_jennifer = initial_cans_jennifer + total_additional_cans # eval: 94.0 = 40 + 54.0

    #: FA
    answer = total_cans_jennifer
    return answer # eval: return 94.0
