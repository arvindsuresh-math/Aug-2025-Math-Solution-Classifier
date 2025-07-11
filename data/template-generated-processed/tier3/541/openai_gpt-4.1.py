def solve():
    """Index: 541.
    Returns: the number of lego sets Tonya buys for her older sister.
    """
    # L1
    dolls_bought = 4 # 4 dolls that cost $15 each
    doll_price = 15 # $15 each
    spent_on_younger = dolls_bought * doll_price

    # L2
    lego_price = 20 # They cost $20 each
    lego_sets_bought = spent_on_younger / lego_price

    # FA
    answer = lego_sets_bought
    return answer