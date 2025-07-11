def solve():
    """Index: 71.
    Returns: the number of dollars Hillary is left with after making the deposit.
    """
    # L1
    num_crafts_sold = 3 # sells 3 crafts
    price_per_craft = 12 # 12 dollars per craft
    initial_sales_revenue = num_crafts_sold * price_per_craft

    # L2
    extra_dollars_from_customer = 7 # an extra 7 dollars from an appreciative customer
    total_after_extra = initial_sales_revenue + extra_dollars_from_customer

    # L3
    amount_deposited = 18 # deposits 18 dollars
    remaining_after_deposit = total_after_extra - amount_deposited

    # FA
    answer = remaining_after_deposit
    return answer