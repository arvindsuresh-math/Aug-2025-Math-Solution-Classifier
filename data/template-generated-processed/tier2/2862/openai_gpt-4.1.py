def solve():
    """Index: 2862.
    Returns: the total cost of Emily's entire order including installation.
    """
    # L1
    num_curtains = 2 # 2 pairs of curtains
    curtain_price = 30.00 # $30.00 each
    curtains_total = num_curtains * curtain_price

    # L2
    num_prints = 9 # 9 wall prints
    print_price = 15.00 # $15.00 each
    prints_total = num_prints * print_price

    # L3
    installation_fee = 50.00 # installation service is $50.00
    total_cost = curtains_total + prints_total + installation_fee

    # FA
    answer = total_cost
    return answer