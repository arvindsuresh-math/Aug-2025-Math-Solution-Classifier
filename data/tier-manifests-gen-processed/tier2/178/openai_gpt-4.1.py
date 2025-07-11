def solve():
    """Index: 178.
    Returns: the amount of change Simon receives back from his purchase.
    """
    # L1
    num_pansies = 5 # 5 pansies
    pansy_price = 2.50 # $2.50 each
    pansies_total = num_pansies * pansy_price

    # L2
    num_petunias = 5 # 5 petunias
    petunia_price = 1.00 # $1.00 each
    petunias_total = num_petunias * petunia_price

    # L3
    hydrangea_price = 12.50 # one hydrangea that cost $12.50
    total_before_discount = pansies_total + hydrangea_price + petunias_total

    # L4
    discount_percent = 0.10 # 10% off
    discount_amount = total_before_discount * discount_percent

    # L5
    total_after_discount = total_before_discount - discount_amount

    # L6
    bill_amount = 50 # paid with a $50 bill
    change = bill_amount - total_after_discount

    # FA
    answer = change
    return answer