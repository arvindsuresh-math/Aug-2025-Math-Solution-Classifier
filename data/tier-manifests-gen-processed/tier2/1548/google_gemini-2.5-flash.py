def solve():
    """Index: 1548.
    Returns: the number of bugs left in the garden.
    """
    # L1
    spray_reduction_percent_num = 80 # reduces the total bug population to 80%
    initial_bug_population = 400 # 400 bugs to start
    percent_factor = 0.01 # WK
    bugs_after_spray = spray_reduction_percent_num * percent_factor * initial_bug_population

    # L2
    num_spiders = 12 # introduces 12 spiders
    bugs_per_spider = 7 # eats 7 bugs
    bugs_eaten_by_spiders = num_spiders * bugs_per_spider

    # L3
    remaining_bugs = bugs_after_spray - bugs_eaten_by_spiders

    # FA
    answer = remaining_bugs
    return answer