def solve():
    """Index: 6782.
    Returns: the price Gerald paid for his guitar.
    """
    # L2
    hendricks_price = 200 # Hendricks buys a guitar for $200
    discount_rate = 0.20 # 20% less
    factor_of_gerald_price = 1 - discount_rate

    # L3
    gerald_price = hendricks_price / factor_of_gerald_price

    # FA
    answer = gerald_price
    return answer