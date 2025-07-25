def solve():
    """Index: 495.
    Returns: the number of items each baggie has.
    """
    # L1
    pretzels = 64 # 64 pretzels
    goldfish_multiplier = 4 # four times as many goldfish
    goldfish = pretzels * goldfish_multiplier

    # L2
    suckers = 32 # 32 suckers
    total_snacks = goldfish + pretzels + suckers

    # L3
    num_kids = 16 # 16 kids
    snacks_per_baggie = total_snacks / num_kids

    # FA
    answer = snacks_per_baggie
    return answer