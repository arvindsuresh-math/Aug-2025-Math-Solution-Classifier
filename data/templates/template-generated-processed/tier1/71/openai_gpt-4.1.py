def solve():
    """Index: 71.
    Returns: the number of dollars Hillary is left with after making the deposit.
    """
    # L1
    crafts_sold = 3 # Hillary sells 3 crafts
    price_per_craft = 12 # 12 dollars per craft
    sales_total = crafts_sold * price_per_craft

    # L2
    extra_from_customer = 7 # extra 7 dollars from an appreciative customer
    total_money = sales_total + extra_from_customer

    # L3
    deposit_amount = 18 # deposits 18 dollars
    money_left = total_money - deposit_amount

    # FA
    answer = money_left
    return answer