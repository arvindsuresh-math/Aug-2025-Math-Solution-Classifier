def solve(
    sam_skips_per_round: int = 16, # Sam skipped 16 times in each round
    round1_diff: int = 1, # Sam completed 1 more skip than Jeff in the first round
    round2_diff: int = 3, # Jeff skipped 3 fewer times than Sam in the second round
    round3_diff: int = 4, # Jeff skipped 4 more times than Sam in the third round
    round4_ratio: float = 0.5 # Jeff completed half the number of skips as Sam in the last round
):
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """

    #: L1
    jeff_round1 = sam_skips_per_round - round1_diff # eval: 15 = 16 - 1

    #: L2
    jeff_round2 = sam_skips_per_round - round2_diff # eval: 13 = 16 - 3

    #: L3

    #: L4
    jeff_round4 = sam_skips_per_round * round4_ratio # eval: 8.0 = 16 * 0.5

    #: L5
    jeff_total_skips = jeff_round1 + jeff_round2 + round4_ratio + jeff_round4 # eval: 36.5 = 15 + 13 + 0.5 + 8.0

    #: L6
    jeff_avg_skips = jeff_total_skips / 4 # eval: 9.125 = 36.5 / 4

    #: FA
    answer = jeff_avg_skips
    return answer # eval: return 9.125
