def solve():
    """Index: 123.
    Returns: how much more expensive, per can, in cents, the grocery store deal is.
    """
    # L1
    warehouse_cans = 48 # 48 cans of sparkling water
    warehouse_price_dollars = 12.00 # $12.00 a case
    warehouse_cost_per_can_dollars = warehouse_price_dollars / warehouse_cans

    # L2
    grocery_cans = 12 # 12 cans
    grocery_price_dollars = 6.00 # $6.00
    grocery_cost_per_can_dollars = grocery_price_dollars / grocery_cans

    # L3
    difference_per_can_dollars = grocery_cost_per_can_dollars - warehouse_cost_per_can_dollars

    # FA
    cents_per_dollar = 100 # WK
    answer = difference_per_can_dollars * cents_per_dollar
    return answer