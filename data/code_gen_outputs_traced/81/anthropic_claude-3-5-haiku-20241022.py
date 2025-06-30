def solve(
        sam_skips_per_round: int = 16,  # Sam skipped 16 times in each round
        rounds: int = 4  # The competition was split into four rounds
    ):
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """

    #: L1
    jeff_skips_round1 = sam_skips_per_round - 1 # eval: 15 = 16 - 1

    #: L2
    jeff_skips_round2 = sam_skips_per_round - 3 # eval: 13 = 16 - 3

    #: L3
    jeff_skips_round3 = sam_skips_per_round + 4 # eval: 20 = 16 + 4

    #: L4
    jeff_skips_round4 = sam_skips_per_round / 2 # eval: 8.0 = 16 / 2

    #: L5
    total_jeff_skips = jeff_skips_round1 + jeff_skips_round2 + jeff_skips_round3 + jeff_skips_round4 # eval: 56.0 = 15 + 13 + 20 + 8.0

    #: L6
    average_jeff_skips = total_jeff_skips / rounds # eval: 14.0 = 56.0 / 4

    #: FA
    answer = average_jeff_skips
    return answer # eval: return 14.0
