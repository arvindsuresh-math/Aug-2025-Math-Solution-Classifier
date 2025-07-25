def solve():
    """Index: 6195.
    Returns: the total number of pink crayons Mara and Luna have.
    """
    # L1
    mara_total_crayons = 40 # Mara has 40 crayons
    mara_pink_percentage_numerator = 10 # 10 percent of her crayons
    percentage_denominator = 100 # WK
    mara_pink_crayons = mara_total_crayons * (mara_pink_percentage_numerator / percentage_denominator)

    # L2
    luna_total_crayons = 50 # Luna has 50 crayons
    luna_pink_percentage_numerator = 20 # 20 percent of them
    luna_pink_crayons = luna_total_crayons * (luna_pink_percentage_numerator / percentage_denominator)

    # L3
    total_pink_crayons = mara_pink_crayons + luna_pink_crayons

    # FA
    answer = total_pink_crayons
    return answer