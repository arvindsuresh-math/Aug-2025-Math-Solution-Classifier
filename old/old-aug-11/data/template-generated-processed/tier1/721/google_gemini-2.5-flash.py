def solve():
    """Index: 721.
    Returns: the total cost to buy one of each of the three mentioned products.
    """
    # L1
    smartphone_price = 300 # smartphones for $300 each
    pc_price_more_than_smartphone = 500 # personal computers for $500 more than smartphones
    pc_price = smartphone_price + pc_price_more_than_smartphone

    # L2
    tablet_price = smartphone_price + pc_price

    # L3
    total_cost = smartphone_price + pc_price + tablet_price

    # FA
    answer = total_cost
    return answer