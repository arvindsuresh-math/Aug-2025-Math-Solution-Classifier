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
    jeff_round1 = sam_skips_per_round - round1_diff

    #: L2
    jeff_round2 = sam_skips_per_round - round2_diff

    #: L3
    jeff_round3 = sam_skips_per_round + round3_diff

    #: L4
    jeff_round4 = sam_skips_per_round * round4_ratio

    #: L5
    jeff_total_skips = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    #: L6
    jeff_avg_skips = jeff_total_skips / 4

    answer = jeff_avg_skips # FINAL ANSWER
    return answer