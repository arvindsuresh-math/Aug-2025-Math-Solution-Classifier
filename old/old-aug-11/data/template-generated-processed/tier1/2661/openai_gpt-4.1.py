def solve():
    """Index: 2661.
    Returns: the total price Romina paid for 20 boxes after the price reduction.
    """
    # L1
    initial_price = 104 # initial price was $104
    price_reduction = 24 # reduced by $24
    new_price = initial_price - price_reduction

    # L2
    num_boxes = 20 # Romina bought 20 of such boxes
    total_price = num_boxes * new_price

    # FA
    answer = total_price
    return answer