def solve():
    """Index: 2380.
    Returns: the number of ounces of milk James has left.
    """
    # L1
    initial_gallons = 3 # 3 gallons of milk
    ounces_per_gallon = 128 # 128 ounces in a gallon
    initial_ounces = initial_gallons * ounces_per_gallon

    # L2
    drank_ounces = 13 # drank 13 ounces of the milk
    remaining_ounces = initial_ounces - drank_ounces

    # FA
    answer = remaining_ounces
    return answer