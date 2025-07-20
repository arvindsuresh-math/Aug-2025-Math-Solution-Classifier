def solve():
    """Index: 7451.
    Returns: how much more profit they make per month selling motorcycles instead of cars.
    """
    # L1
    num_cars_made = 4 # make 4 cars
    car_sale_price = 50 # sold each car for $50
    car_sales_revenue = num_cars_made * car_sale_price

    # L2
    car_materials_cost = 100 # cost $100 for materials
    car_profit = car_sales_revenue - car_materials_cost

    # L3
    num_motorcycles_sold = 8 # sell 8 of them
    motorcycle_sale_price = 50 # for $50 each
    motorcycle_sales_revenue = num_motorcycles_sold * motorcycle_sale_price

    # L4
    motorcycle_materials_cost = 250 # it costs $250 for materials
    motorcycle_profit = motorcycle_sales_revenue - motorcycle_materials_cost

    # L5
    profit_difference = motorcycle_profit - car_profit

    # FA
    answer = profit_difference
    return answer