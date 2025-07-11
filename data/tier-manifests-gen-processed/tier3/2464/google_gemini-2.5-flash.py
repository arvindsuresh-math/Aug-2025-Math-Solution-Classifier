def solve():
    """Index: 2464.
    Returns: the number of tablespoons of soap to add.
    """
    # L1
    container_capacity_oz = 40 # can hold 40 ounces of liquid
    ounces_per_cup = 8 # 8 ounces in a cup of water
    container_capacity_cups = container_capacity_oz / ounces_per_cup

    # L2
    soap_per_cup = 3 # 3 tablespoons of soap for every 1 cup of water
    total_soap_tablespoons = container_capacity_cups * soap_per_cup

    # FA
    answer = total_soap_tablespoons
    return answer