def solve():
    """Index: 1677.
    Returns: the additional amount Danny should order to get free delivery.
    """
    # L1
    burger_price = 3.20 # $3.20 each (quarter-pounder burgers)
    burger_qty = 2 # 2 quarter-pounder burgers
    burger_total = burger_price * burger_qty

    # L2
    fries_price = 1.90 # $1.90 each (large fries)
    fries_qty = 2 # 2 large fries
    fries_total = fries_qty * fries_price

    # L3
    shake_price = 2.40 # $2.40 each (milkshakes)
    shake_qty = 2 # 2 milkshakes
    shake_total = shake_qty * shake_price

    # L4
    total_spent = burger_total + fries_total + shake_total

    # L5
    min_free_delivery = 18 # minimum purchase of $18
    additional_needed = min_free_delivery - total_spent

    # FA
    answer = additional_needed
    return answer