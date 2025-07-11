def solve():
    """Index: 81.
    Returns: the average number of skips per round completed by Jeff.
    """
    # L1
    sam_skips_per_round = 16 # Sam skipped 16 times in each round
    sam_advantage_round_1 = 1 # Sam completed 1 more skip than Jeff in the first round
    jeff_skips_round_1 = sam_skips_per_round - sam_advantage_round_1

    # L2
    sam_advantage_round_2 = 3 # Jeff skipped 3 fewer times than Sam in the second round
    jeff_skips_round_2 = sam_skips_per_round - sam_advantage_round_2

    # L3
    jeff_advantage_round_3 = 4 # Jeff skipped 4 more times than Sam in the third round
    jeff_skips_round_3 = sam_skips_per_round + jeff_advantage_round_3

    # L4
    half_divisor = 2 # only completed half the number of skips as Sam
    jeff_skips_round_4 = sam_skips_per_round / half_divisor

    # L5
    total_jeff_skips = jeff_skips_round_1 + jeff_skips_round_2 + jeff_skips_round_3 + jeff_skips_round_4

    # L6
    number_of_rounds = 4 # The competition was split into four rounds
    average_jeff_skips = total_jeff_skips / number_of_rounds

    # FA
    answer = average_jeff_skips
    return answer