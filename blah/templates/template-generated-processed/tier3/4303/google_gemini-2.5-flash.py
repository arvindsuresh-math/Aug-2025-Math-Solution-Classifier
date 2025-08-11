def solve():
    """Index: 4303.
    Returns: the total number of chickens on the poultry farm.
    """
    # L1
    hens = 12 # Jeffrey owns a poultry farm with 12 hens
    hens_per_rooster = 3 # For every 3 hens, there is 1 rooster
    roosters = hens / hens_per_rooster

    # L2
    chicks_per_hen = 5 # Each hen has 5 chicks
    chicks = hens * chicks_per_hen

    # L3
    total_chickens = hens + roosters + chicks

    # FA
    answer = total_chickens
    return answer