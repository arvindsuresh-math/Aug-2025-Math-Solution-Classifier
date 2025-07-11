def solve():
    """Index: 1423.
    Returns: the number of countries Zack traveled to.
    """
    # L1
    george_countries = 6 # If George traveled to 6 countries
    joseph_divisor = 2 # Joseph traveled to half the number of countries
    joseph_countries = george_countries / joseph_divisor

    # L2
    patrick_multiplier = 3 # Patrick traveled to three times the number of countries Joseph traveled to
    patrick_countries = joseph_countries * patrick_multiplier

    # L3
    zack_multiplier = 2 # Zack has traveled to twice the number of countries Patrick traveled to
    zack_countries = zack_multiplier * patrick_countries

    # FA
    answer = zack_countries
    return answer