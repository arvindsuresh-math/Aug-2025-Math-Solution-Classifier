def solve():
    """Index: 7205.
    Returns: the total amount Marc spent.
    """
    # L1
    num_cars = 5 # 5 model cars
    cost_per_car = 20 # cost $20 each
    cost_cars = cost_per_car * num_cars

    # L2
    num_paint_bottles = 5 # 5 bottles of paint
    cost_per_paint_bottle = 10 # cost $10 each
    cost_paint = cost_per_paint_bottle * num_paint_bottles

    # L3
    num_paintbrushes = 5 # 5 paintbrushes
    cost_per_paintbrush = 2 # cost $2 each
    cost_paintbrushes = cost_per_paintbrush * num_paintbrushes

    # L4
    total_spent = cost_cars + cost_paint + cost_paintbrushes

    # FA
    answer = total_spent
    return answer