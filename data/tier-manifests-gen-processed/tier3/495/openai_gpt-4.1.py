def solve():
    """Index: 495.
    Returns: the number of snack items in each baggie.
    """
    # L1
    pretzels = 64 # 64 pretzels
    goldfish_per_pretzel = 4 # four times as many goldfish
    goldfish = pretzels * goldfish_per_pretzel

    # L2
    suckers = 32 # 32 suckers
    total_snacks = goldfish + pretzels + suckers

    # L3
    baggies = 16 # 16 kids in the class
    snacks_per_baggie = total_snacks / baggies

    # FA
    answer = snacks_per_baggie
    return answer