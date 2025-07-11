def solve():
    """Index: 1081.
    Returns: the total amount of honey produced by both hives in liters.
    """
    # L1
    hive1_bees = 1000 # One of the hives has 1000 bees
    hive2_fewer_percent_num = 20 # 20% fewer bees
    percent_factor = 0.01 # WK
    hive2_fewer_bees = hive2_fewer_percent_num / 100 * hive1_bees

    # L2
    hive2_bees = hive1_bees - hive2_fewer_bees

    # L3
    hive1_honey = 500 # produces 500 liters of honey
    honey_per_bee_hive1 = hive1_honey / hive1_bees

    # L4
    hive2_honey_increase_factor = 1.4 # each bee produces 40% more honey
    honey_per_bee_hive2 = hive2_honey_increase_factor * honey_per_bee_hive1

    # L5
    # Note: The solution mapping uses 700 bees in L5, but L2 computes 800 bees. This is likely a typo in the solution mapping. We'll use hive2_bees as computed.
    hive2_honey = honey_per_bee_hive2 * hive2_bees

    # L6
    total_honey = hive2_honey + hive1_honey

    # FA
    answer = total_honey
    return answer