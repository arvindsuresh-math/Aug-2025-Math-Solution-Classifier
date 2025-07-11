def solve():
    """Index: 2932.
    Returns: how many more tools the Target multitool has compared to Walmart.
    """
    # L1
    walmart_screwdriver = 1 # a screwdriver
    walmart_knives = 3 # 3 knives
    walmart_other_tools = 2 # two other tools
    walmart_total = walmart_screwdriver + walmart_knives + walmart_other_tools

    # L2
    target_knives_multiplier = 2 # twice as many knives as Walmart
    target_knives = walmart_knives * target_knives_multiplier

    # L3
    target_screwdriver = 1 # a screwdriver
    target_files = 3 # three files
    target_scissors = 1 # a pair of scissors
    target_total = target_screwdriver + target_knives + target_files + target_scissors

    # L4
    difference = target_total - walmart_total

    # FA
    answer = difference
    return answer