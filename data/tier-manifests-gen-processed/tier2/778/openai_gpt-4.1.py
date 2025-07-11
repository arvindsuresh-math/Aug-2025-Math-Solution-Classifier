def solve():
    """Index: 778.
    Returns: the total out-of-pocket cost for James after all transactions.
    """
    # L1
    tv_cost = 700 # TV that cost $700
    returned_bike_cost = 500 # bike that cost $500
    returned_items_value = tv_cost + returned_bike_cost

    # L2
    total_purchase = 3000 # buys $3000 worth of stuff
    out_after_returns = total_purchase - returned_items_value

    # L3
    percent_more = 0.2 # 20% more
    multiplier = 1 + percent_more

    # L4
    sold_bike_cost = returned_bike_cost * multiplier

    # L5
    sell_percent = 0.8 # 80% of what he bought it for
    sold_bike_sale_price = sold_bike_cost * sell_percent

    # L6
    out_on_sold_bike = sold_bike_cost - sold_bike_sale_price

    # L7
    out_after_bike_sale = out_after_returns + out_on_sold_bike

    # L8
    toaster_cost = 100 # toaster for $100
    answer = out_after_bike_sale + toaster_cost
    return answer