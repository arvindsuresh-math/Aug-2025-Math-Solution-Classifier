def solve():
    """Index: 6650.
    Returns: the number of bottles of sanitizer gel the Drugstore has at the end of the week.
    """
    # L1
    sold_monday = 2445 # On Monday 2445 bottles were sold
    sold_tuesday = 900 # on Tuesday 900 bottles were sold
    sold_mon_tue = sold_monday + sold_tuesday

    # L2
    days_rest_of_week = 5 # WK
    sold_per_day_rest_of_week = 50 # 50 bottles each day for the rest of the week were sold
    sold_rest_of_week = days_rest_of_week * sold_per_day_rest_of_week

    # L3
    total_sold_week = sold_mon_tue + sold_rest_of_week

    # L4
    initial_inventory = 4500 # 4500 bottles of hand sanitizer gel in inventory at the beginning of the week
    remaining_after_sales = initial_inventory - total_sold_week

    # L5
    delivery_saturday = 650 # On Saturday, the supplier delivers an order for 650 bottles
    final_inventory = remaining_after_sales + delivery_saturday

    # FA
    answer = final_inventory
    return answer