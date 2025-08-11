def solve():
    """Index: 1154.
    Returns: the total cost of the stockings.
    """
    # L1
    num_grandchildren = 5 # 5 grandchildren
    num_children = 4 # 4 children
    total_stockings = num_grandchildren + num_children

    # L2
    stocking_price_each = 20.00 # $20.00 each
    discount_percent_num = 10 # 10% off
    discount_percent_decimal = 0.10 # currently 10% off
    discount_amount_per_stocking = stocking_price_each * discount_percent_decimal

    # L3
    price_after_discount_per_stocking = stocking_price_each - discount_amount_per_stocking

    # L4
    total_stocking_cost_after_discount = price_after_discount_per_stocking * total_stockings

    # L5
    monogramming_cost_per_stocking = 5.00 # $5.00 per stocking
    total_monogramming_cost = total_stockings * monogramming_cost_per_stocking

    # L6
    final_total_cost = total_stocking_cost_after_discount + total_monogramming_cost

    # FA
    answer = final_total_cost
    return answer