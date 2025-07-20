def solve():
    """Index: 5283.
    Returns: the amount Cody paid.
    """
    # L1
    initial_price = 40 # $40 worth of stuff
    tax_rate = 0.05 # The taxes were 5%
    taxes_amount = initial_price * tax_rate

    # L2
    price_after_taxes = initial_price + taxes_amount

    # L3
    discount_amount = 8 # got an $8 discount
    price_after_discount = price_after_taxes - discount_amount

    # L4
    split_divisor = 2 # split the final price equally
    cody_paid = price_after_discount / split_divisor

    # FA
    answer = cody_paid
    return answer