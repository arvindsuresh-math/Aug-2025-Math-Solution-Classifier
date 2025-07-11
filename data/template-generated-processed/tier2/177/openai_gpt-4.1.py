def solve():
    """Index: 177.
    Returns: the amount James was out of pocket for the car replacement.
    """
    # L1
    old_car_value = 20000 # $20,000 car
    old_car_sale_percent = 0.8 # sold for 80% of its value
    old_car_sale_price = old_car_value * old_car_sale_percent

    # L2
    new_car_sticker_price = 30000 # $30,000 sticker price car
    new_car_purchase_percent = 0.9 # 90% of its value
    new_car_purchase_price = new_car_sticker_price * new_car_purchase_percent

    # L3
    out_of_pocket = new_car_purchase_price - old_car_sale_price

    # FA
    answer = out_of_pocket
    return answer