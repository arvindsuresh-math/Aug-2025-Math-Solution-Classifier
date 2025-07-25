def solve():
    """Index: 7199.
    Returns: the total amount Henry gets paid for selling and painting 8 bikes.
    """
    # L1
    paint_payment = 5 # If Henry gets $5 to paint the bike
    sell_more_than_paint = 8 # For every bike Henry sells, he is paid $8 more than he is paid to paint the bike
    sell_payment = paint_payment + sell_more_than_paint
    total_per_bike = paint_payment + sell_payment

    # L2
    num_bikes = 8 # 8 bikes
    total_paid = num_bikes * total_per_bike

    # FA
    answer = total_paid
    return answer