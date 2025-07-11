def solve():
    """Index: 778.
    Returns: the total amount James is out of pocket.
    """
    # L1
    returned_tv_cost = 700 # TV that cost $700
    returned_bike_cost = 500 # bike that cost $500
    total_returned_value = returned_tv_cost + returned_bike_cost

    # L2
    initial_amazon_spend = 3000 # $3000 worth of stuff from Amazon
    current_out_of_pocket = initial_amazon_spend - total_returned_value

    # L3
    base_multiplier = 1 # WK
    percentage_increase_decimal = 0.2 # 20% more
    increase_factor = base_multiplier + percentage_increase_decimal

    # L4
    sold_bike_original_cost = returned_bike_cost * increase_factor

    # L5
    sale_price_percent = 0.8 # 80% of what he bought it for
    sold_bike_sale_price = sold_bike_original_cost * sale_price_percent

    # L6
    bike_loss = sold_bike_original_cost - sold_bike_sale_price

    # L7
    out_of_pocket_after_bike_sale = current_out_of_pocket + bike_loss

    # L8
    toaster_cost = 100 # buys a toaster for $100
    final_out_of_pocket = out_of_pocket_after_bike_sale + toaster_cost

    # FA
    answer = final_out_of_pocket
    return answer