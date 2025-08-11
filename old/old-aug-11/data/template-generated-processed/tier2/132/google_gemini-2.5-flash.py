def solve():
    """Index: 132.
    Returns: the total amount James paid for the beef.
    """
    # L1
    num_packs = 5 # 5 packs of beef
    pounds_per_pack = 4 # 4 pounds each
    total_pounds = num_packs * pounds_per_pack

    # L2
    price_per_pound = 5.50 # $5.50 per pound
    total_cost = total_pounds * price_per_pound

    # FA
    answer = total_cost
    return answer