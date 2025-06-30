def solve(
    sam_skips_per_round: int = 16,  # Sam skipped 16 times in each round
    rounds: int = 4  # The competition was split into four rounds
):
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """

    #: L1

    #: L2
    jeff_round2 = sam_skips_per_round - 3

    #: L3
    jeff_round3 = sam_skips_per_round + 4

    #: L4
    jeff_round4 = sam_skips_per_round / 2

    #: L5
    total_jeff_skips = rounds + jeff_round2 + jeff_round3 + jeff_round4

    #: L6
    average_jeff_skips = total_jeff_skips / rounds

    #: FA
    answer = average_jeff_skips
    return answer