def solve():
    """Index: 1262.
    Returns: the number of pints of coffee Genevieve drank.
    """
    # L1
    total_gallons = 4.5 # 4.5 gallons of coffee
    pints_per_gallon = 8 # WK: 1 gallon = 8 pints
    total_pints = total_gallons * pints_per_gallon

    # L2
    num_thermoses = 18 # 18 thermoses
    pints_per_thermos = total_pints / num_thermoses

    # L3
    genevieve_thermoses = 3 # Genevieve drank 3 thermoses
    genevieve_pints = pints_per_thermos * genevieve_thermoses

    # FA
    answer = genevieve_pints
    return answer