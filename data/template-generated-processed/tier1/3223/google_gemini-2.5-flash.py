def solve():
    """Index: 3223.
    Returns: the number of roosters on the farm.
    """
    # L1
    total_chickens = 9000 # 9,000 chickens
    rooster_ratio = 2 # roosters outnumber the hens 2 to 1
    hen_ratio = 1 # roosters outnumber the hens 2 to 1
    hens = total_chickens / (rooster_ratio + hen_ratio)

    # L2
    roosters = hens * rooster_ratio

    # FA
    answer = roosters
    return answer