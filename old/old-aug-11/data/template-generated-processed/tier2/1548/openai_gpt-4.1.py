def solve():
    """Index: 1548.
    Returns: the number of bugs left after spraying and introducing spiders.
    """
    # L1
    spray_percent_num = 80 # reduces to 80% of what it was previously
    percent_factor = 0.01 # WK
    initial_bug_count = 400 # garden has 400 bugs to start
    bugs_after_spray = spray_percent_num * percent_factor * initial_bug_count

    # L2
    num_spiders = 12 # introduces 12 spiders
    bugs_per_spider = 7 # each spider eats 7 bugs
    bugs_eaten_by_spiders = num_spiders * bugs_per_spider

    # L3
    final_bug_count = bugs_after_spray - bugs_eaten_by_spiders

    # FA
    answer = final_bug_count
    return answer