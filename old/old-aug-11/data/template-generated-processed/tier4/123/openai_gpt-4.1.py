def solve():
    """Index: 123.
    Returns: the difference in price per can (in cents) between the grocery store and the warehouse.
    """
    # L1
    warehouse_total_cans = 48 # 48 cans of sparkling water for $12.00 a case
    warehouse_total_dollars = 12.00 # $12.00 a case
    warehouse_price_per_can = warehouse_total_dollars / warehouse_total_cans

    # L2
    grocery_total_cans = 12 # 12 cans for $6.00
    grocery_total_dollars = 6.00 # $6.00
    grocery_price_per_can = grocery_total_dollars / grocery_total_cans

    # L3
    price_difference_dollars = grocery_price_per_can - warehouse_price_per_can
    cents_per_dollar = 100 # WK
    price_difference_cents = price_difference_dollars * cents_per_dollar

    # FA
    answer = price_difference_cents
    return answer