def solve(
    num_rounds: int = 4, # split into four rounds
    diff_round1: int = 1, # 1 more skip than Jeff in the first round
    diff_round2: int = 3, # 3 fewer times than Sam in the second round
    diff_round3: int = 4, # 4 more times than Sam in the third round
    fraction_round4: float = 0.5, # only completed half the number of skips as Sam in the last round
    sam_skips_per_round: int = 16 # Sam skipped 16 times in each round
):
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """

    #: L1
    jeff_skips_round1 = sam_skips_per_round - diff_round1 # eval: 15 = 16 - 1

    #: L2
    jeff_skips_round2 = sam_skips_per_round - diff_round2 # eval: 13 = 16 - 3

    #: L3
    jeff_skips_round3 = sam_skips_per_round + diff_round3 # eval: 20 = 16 + 4

    #: L4
    jeff_skips_round4 = sam_skips_per_round * fraction_round4 # eval: 8.0 = 16 * 0.5

    #: L5
    jeff_total_skips = jeff_skips_round1 - jeff_skips_round2 + jeff_skips_round3 + jeff_skips_round4 # eval: 30.0 = 15 - 13 + 20 + 8.0

    #: L6
    jeff_average_skips = jeff_total_skips / num_rounds # eval: 7.5 = 30.0 / 4

    #: FA
    answer = jeff_average_skips
    return answer # eval: return 7.5
