def solve():
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """
    # L1
    sam_skips_per_round = 16 # Sam skipped 16 times in each round
    round1_difference = 1 # Sam completed 1 more skip than Jeff in the first round
    jeff_round1 = sam_skips_per_round - round1_difference

    # L2
    round2_difference = 3 # Jeff skipped 3 fewer times than Sam in the second round
    jeff_round2 = sam_skips_per_round - round2_difference

    # L3
    round3_difference = 4 # Jeff skipped 4 more times than Sam in the third round
    jeff_round3 = sam_skips_per_round + round3_difference

    # L4
    round4_divisor = 2 # Jeff only completed half the number of skips as Sam in the last round
    jeff_round4 = sam_skips_per_round / round4_divisor

    # L5
    jeff_total_skips = jeff_round1 + jeff_round2 + jeff_round3 + jeff_round4

    # L6
    total_rounds = 4 # The competition was split into four rounds
    jeff_average = jeff_total_skips / total_rounds

    # FA
    answer = jeff_average
    return answer