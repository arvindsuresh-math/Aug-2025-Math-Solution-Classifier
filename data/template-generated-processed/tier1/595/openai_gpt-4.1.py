def solve():
    """Index: 595.
    Returns: the number of bananas Donna has.
    """
    # L1
    lydia_bananas = 60 # Lydia has 60 bananas
    dawn_more_than_lydia = 40 # Dawn has 40 more bananas than Lydia
    dawn_bananas = lydia_bananas + dawn_more_than_lydia

    # L2
    dawn_lydia_total = dawn_bananas + lydia_bananas

    # L3
    total_bananas = 200 # total of 200 bananas
    donna_bananas = total_bananas - dawn_lydia_total

    # FA
    answer = donna_bananas
    return answer