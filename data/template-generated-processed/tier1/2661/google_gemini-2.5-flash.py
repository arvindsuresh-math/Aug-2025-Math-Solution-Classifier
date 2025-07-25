def solve():
    """Index: 2661.
    Returns: the total price Romina paid for the cereal boxes.
    """
    # L1
    initial_price = 104 # initial price was $104
    price_reduction = 24 # reduced by $24
    new_price = initial_price - price_reduction

    # L2
    num_boxes_bought = 20 # bought 20 of such boxes
    total_price_paid = num_boxes_bought * new_price

    # FA
    answer = total_price_paid
    return answer