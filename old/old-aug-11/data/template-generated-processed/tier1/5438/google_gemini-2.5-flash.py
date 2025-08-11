def solve():
    """Index: 5438.
    Returns: the total number of flower petals in Elena’s garden.
    """
    # L1
    num_lilies = 8 # 8 lilies
    petals_per_lily = 6 # Each lily has 6 petals
    lily_petals = num_lilies * petals_per_lily

    # L2
    num_tulips = 5 # 5 tulips
    petals_per_tulip = 3 # Each tulip has 3 petals
    tulip_petals = num_tulips * petals_per_tulip

    # L3
    total_petals = lily_petals + tulip_petals

    # FA
    answer = total_petals
    return answer