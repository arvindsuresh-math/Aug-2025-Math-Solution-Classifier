def solve():
    """Index: 4714.
    Returns: the percentage of frogs that have mutated, rounded to the nearest integer.
    """
    # L1
    frogs_extra_legs = 5 # 5 frogs with extra legs
    frogs_two_heads = 2 # 2 frogs with 2 heads
    frogs_bright_red = 2 # two frogs that are bright red
    total_mutant_frogs = frogs_extra_legs + frogs_two_heads + frogs_bright_red

    # L2
    normal_frogs = 18 # 18 normal frogs
    total_frogs = total_mutant_frogs + normal_frogs

    # L3
    percent_multiplier = 100 # WK
    mutant_percentage_raw = (total_mutant_frogs / total_frogs) * percent_multiplier
    mutant_percentage_rounded = round(mutant_percentage_raw)

    # FA
    answer = mutant_percentage_rounded
    return answer