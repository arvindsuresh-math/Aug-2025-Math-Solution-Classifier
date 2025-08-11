def solve():
    """Index: 6309.
    Returns: how much more profit Maddox got from the sale of his cameras than Theo.
    """
    # L1
    num_cameras = 3 # both bought 3 Polaroid Cameras
    cost_per_camera = 20 # $20 per camera
    total_cost_initial = num_cameras * cost_per_camera

    # L2
    maddox_sell_price_per_camera = 28 # sold his cameras at $28 each
    maddox_total_revenue = maddox_sell_price_per_camera * num_cameras

    # L3
    maddox_profit = maddox_total_revenue - total_cost_initial

    # L4
    theo_sell_price_per_camera = 23 # sold his cameras at $23 each
    theo_total_revenue = theo_sell_price_per_camera * num_cameras

    # L5
    theo_profit = theo_total_revenue - total_cost_initial

    # L6
    profit_difference = maddox_profit - theo_profit

    # FA
    answer = profit_difference
    return answer