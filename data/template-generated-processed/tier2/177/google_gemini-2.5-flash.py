def solve():
    """Index: 177.
    Returns: how much James was out of pocket.
    """
    # L1
    original_car_value = 20000 # $20,000 car
    sold_percentage = 0.8 # 80% of its value
    sold_price = original_car_value * sold_percentage
    sold_price_text = "16,000" # from solution text for display

    # L2
    new_car_sticker_price = 30000 # $30,000 sticker price car
    bought_percentage = 0.9 # 90% of its value
    bought_price = new_car_sticker_price * bought_percentage
    bought_price_text = "27,000" # from solution text for display

    # L3
    out_of_pocket = bought_price - sold_price
    out_of_pocket_text = "11,000" # from solution text for display

    # FA
    answer = out_of_pocket
    return answer