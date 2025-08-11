def solve():
    """Index: 5962.
    Returns: the amount of discount given in dollars.
    """
    # L1
    tshirt_price = 30 # a t-shirt for $30
    backpack_price = 10 # a backpack for $10
    cap_price = 5 # a blue cap for $5
    total_purchases = tshirt_price + backpack_price + cap_price

    # L2
    amount_paid = 43 # he only spent $43
    discount_amount = total_purchases - amount_paid

    # FA
    answer = discount_amount
    return answer