def solve():
    """Index: 2380.
    Returns: the number of ounces of milk James has left.
    """
    # L1
    gallons = 3 # James has 3 gallons of milk
    ounces_per_gallon = 128 # 128 ounces in a gallon
    initial_ounces = gallons * ounces_per_gallon

    # L2
    drank_ounces = 13 # He drank 13 ounces of the milk
    ounces_left = initial_ounces - drank_ounces

    # FA
    answer = ounces_left
    return answer