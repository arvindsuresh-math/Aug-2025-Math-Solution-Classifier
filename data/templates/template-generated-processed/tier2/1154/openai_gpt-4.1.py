def solve():
    """Index: 1154.
    Returns: the total cost of the stockings including monogramming.
    """
    # L1
    num_grandchildren = 5 # 5 grandchildren
    num_children = 4 # 4 children
    total_stockings = num_grandchildren + num_children

    # L2
    stocking_price = 20.00 # $20.00 each
    discount_percent = 0.10 # 10% off
    discount_amount = stocking_price * discount_percent

    # L3
    discounted_price = stocking_price - discount_amount

    # L4
    stockings_total = discounted_price * total_stockings

    # L5
    monogram_price = 5.00 # $5.00 per stocking
    monogram_total = total_stockings * monogram_price

    # L6
    total_cost = stockings_total + monogram_total

    # FA
    answer = total_cost
    return answer