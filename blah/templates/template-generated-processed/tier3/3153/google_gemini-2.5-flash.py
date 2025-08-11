def solve():
    """Index: 3153.
    Returns: the percentage of animals that are monkeys.
    """
    # L1
    initial_birds = 6 # 6 birds
    eaten_birds = 2 # two of the monkeys each eat one bird
    remaining_birds = initial_birds - eaten_birds

    # L2
    initial_monkeys = 6 # 6 monkeys
    total_animals = initial_monkeys + remaining_birds

    # L3
    percentage_multiplier = 100 # WK
    percent_monkeys = (initial_monkeys / total_animals) * percentage_multiplier

    # FA
    answer = percent_monkeys
    return answer