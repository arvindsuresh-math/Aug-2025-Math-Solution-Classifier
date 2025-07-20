def solve():
    """Index: 6344.
    Returns: the total number of full glasses Daniel can give.
    """
    # L1
    num_jars = 5 # 5 jars of juice
    liters_per_jar = 2 # 2 liters each
    total_liters_juice = num_jars * liters_per_jar

    # L2
    milliliters_per_liter = 1000 # WK
    total_milliliters_juice = total_liters_juice * milliliters_per_liter

    # L3
    ml_per_glass = 250 # 250 milliliters of juice
    num_full_glasses = total_milliliters_juice / ml_per_glass

    # FA
    answer = num_full_glasses
    return answer