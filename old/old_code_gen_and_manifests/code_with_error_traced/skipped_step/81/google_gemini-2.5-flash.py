def solve(
        num_rounds: int = 4, # The competition was split into four rounds
        sam_skips_round1: int = 16, # Sam skipped 16 times in each round
        sam_skips_more_than_jeff_round1: int = 1, # Sam completed 1 more skip than Jeff in the first round
        jeff_skips_fewer_round2: int = 3, # Jeff skipped 3 fewer times than Sam in the second round
        jeff_skips_more_round3: int = 4, # Jeff skipped 4 more times than Sam in the third round
        jeff_skips_factor_round4: float = 0.5 # only completed half the number of skips as Sam in the last round
    ):
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """

    #: L1
    jeff_skips_round1 = sam_skips_round1 - sam_skips_more_than_jeff_round1 # eval: 15 = 16 - 1

    #: L2
    jeff_skips_round2 = sam_skips_round1 - jeff_skips_fewer_round2 # eval: 13 = 16 - 3

    #: L3
    jeff_skips_round3 = sam_skips_round1 + jeff_skips_more_round3 # eval: 20 = 16 + 4

    #: L4

    #: L5
    total_jeff_skips = jeff_skips_round1 + jeff_skips_round2 + jeff_skips_round3 + jeff_skips_fewer_round2 # eval: 51 = 15 + 13 + 20 + 3

    #: L6
    average_jeff_skips_per_round = total_jeff_skips / num_rounds # eval: 12.75 = 51 / 4

    #: FA
    answer = average_jeff_skips_per_round
    return answer # eval: return 12.75
