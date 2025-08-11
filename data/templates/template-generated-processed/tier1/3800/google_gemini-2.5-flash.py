def solve():
    """Index: 3800.
    Returns: the total number of crayons they have.
    """
    # L1
    dina_crayons = 28 # Dina has 28
    jacob_fewer = 2 # two fewer crayons than Dina
    jacob_crayons = dina_crayons - jacob_fewer

    # L2
    wanda_crayons = 62 # Wanda has 62 crayons
    total_crayons = jacob_crayons + wanda_crayons + dina_crayons

    # FA
    answer = total_crayons
    return answer