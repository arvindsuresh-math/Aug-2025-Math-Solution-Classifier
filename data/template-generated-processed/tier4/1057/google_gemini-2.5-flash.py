def solve():
    """Index: 1057.
    Returns: the number of pints of tea Geraldo drank.
    """
    # L1
    gallons_initial = 20 # Twenty gallons of tea
    pints_per_gallon = 8 # WK
    total_pints_tea = gallons_initial * pints_per_gallon

    # L2
    num_containers = 80 # 80 containers
    pints_per_container = total_pints_tea / num_containers

    # L3
    containers_drank_geraldo = 3.5 # Geraldo drank 3.5 containers
    pints_geraldo_drank = containers_drank_geraldo * pints_per_container

    # FA
    answer = pints_geraldo_drank
    return answer