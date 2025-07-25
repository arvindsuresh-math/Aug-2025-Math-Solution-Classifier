def solve():
    """Index: 1057.
    Returns: the number of pints of tea Geraldo drank.
    """
    # L1
    total_gallons = 20 # Twenty gallons of tea
    pints_per_gallon = 8 # WK
    total_pints = total_gallons * pints_per_gallon

    # L2
    num_containers = 80 # 80 containers
    pints_per_container = total_pints / num_containers

    # L3
    geraldo_containers = 3.5 # Geraldo drank 3.5 containers
    geraldo_pints = geraldo_containers * pints_per_container

    # FA
    answer = geraldo_pints
    return answer