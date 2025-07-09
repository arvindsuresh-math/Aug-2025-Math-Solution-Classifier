def solve_81():
    # Sam skipped 16 times in each round
    sam_skips_per_round = 16
    num_rounds = 4

    # Calculate Jeff's skips for each round
    # Round 1: Sam completed 1 more skip than Jeff
    jeff_skips_round1 = sam_skips_per_round - 1

    # Round 2: Jeff skipped 3 fewer times than Sam
    jeff_skips_round2 = sam_skips_per_round - 3

    # Round 3: Jeff skipped 4 more times than Sam
    jeff_skips_round3 = sam_skips_per_round + 4

    # Round 4: Jeff completed half the number of skips as Sam
    jeff_skips_round4 = sam_skips_per_round / 2

    # Calculate Jeff's total skips
    jeff_total_skips = jeff_skips_round1 + jeff_skips_round2 + jeff_skips_round3 + jeff_skips_round4

    # Calculate Jeff's average skips per round
    jeff_average_skips = jeff_total_skips / num_rounds

    return jeff_average_skips

# Execute the function to get the answer
# print(solve_81())