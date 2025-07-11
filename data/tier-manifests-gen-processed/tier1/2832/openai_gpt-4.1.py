def solve():
    """Index: 2832.
    Returns: the total amount the baker earned in April.
    """
    # L1
    cakes_sold = 453 # sold 453 cakes
    cake_price = 12 # at $12
    cake_earnings = cakes_sold * cake_price

    # L2
    pies_sold = 126 # 126 pies
    pie_price = 7 # at $7
    pie_earnings = pies_sold * pie_price

    # L3
    total_earnings = cake_earnings + pie_earnings

    # FA
    answer = total_earnings
    return answer