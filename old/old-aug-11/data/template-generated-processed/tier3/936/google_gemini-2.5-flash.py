def solve():
    """Index: 936.
    Returns: the number of crayons Lizzie has.
    """
    # L1
    billie_crayons = 18 # Billie has 18 crayons
    bobbie_multiplier = 3 # Bobbie has three times as many crayons as Billie
    bobbie_crayons = billie_crayons * bobbie_multiplier

    # L2
    lizzie_divisor = 2 # Lizzie has half as many crayons as Bobbie
    lizzie_crayons = bobbie_crayons / lizzie_divisor

    # FA
    answer = lizzie_crayons
    return answer