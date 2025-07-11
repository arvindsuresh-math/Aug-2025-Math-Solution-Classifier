def solve(
    jennifer_initial_cans: int = 40, # Jennifer purchased 40 cans of milk
    additional_cans_jennifer: int = 6, # bought 6 additional cans
    cans_mark_bought_ratio: int = 5, # for every 5 cans Mark bought
    mark_total_cans: int = 50 # If Mark purchased 50 cans
):
    """Index: 80.
    Returns: the total number of cans of milk Jennifer brought home.
    """

    #: L1
    times_ratio_occurred = mark_total_cans / cans_mark_bought_ratio # eval: 10.0 = 50 / 5

    #: L2
    total_additional_cans = times_ratio_occurred * additional_cans_jennifer # eval: 60.0 = 10.0 * 6

    #: L3

    #: FA
    answer = mark_total_cans
    return answer # eval: return 50
