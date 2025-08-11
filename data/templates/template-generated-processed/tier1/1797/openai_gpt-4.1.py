def solve():
    """Index: 1797.
    Returns: the total amount John spends.
    """
    # L1
    tshirt_price = 20 # t-shirts that cost $20 each
    tshirt_count = 3 # 3 t-shirts
    tshirt_total = tshirt_price * tshirt_count

    # L2
    pants_total = 50 # buys $50 in pants
    total_spent = tshirt_total + pants_total

    # FA
    answer = total_spent
    return answer