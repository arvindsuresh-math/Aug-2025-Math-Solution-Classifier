def solve():
    """Index: 595.
    Returns: the number of bananas Donna has.
    """
    # L1
    lydia_bananas = 60 # Lydia has 60 bananas
    dawn_more_than_lydia = 40 # Dawn has 40 more bananas than Lydia
    dawn_bananas = lydia_bananas + dawn_more_than_lydia

    # L2
    total_dawn_lydia = dawn_bananas + lydia_bananas

    # L3
    total_bananas_all = 200 # total of 200 bananas
    donna_bananas = total_bananas_all - total_dawn_lydia

    # FA
    answer = donna_bananas
    return answer