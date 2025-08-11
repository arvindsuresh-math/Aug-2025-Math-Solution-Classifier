def solve():
    """Index: 4171.
    Returns: the total minutes William spent washing all the vehicles.
    """
    # L1
    window_wash_time = 4 # 4 minutes washing a car’s windows
    body_wash_time = 7 # 7 minutes washing the car body
    tire_clean_time = 4 # 4 minutes cleaning the tires
    wax_time = 9 # 9 minutes waxing the car
    normal_car_time = window_wash_time + body_wash_time + tire_clean_time + wax_time

    # L2
    num_normal_cars = 2 # washed 2 normal cars
    total_normal_cars_time = normal_car_time * num_normal_cars

    # L3
    multiplier_for_suv = 2 # took twice as long as a normal car
    suv_time = normal_car_time * multiplier_for_suv

    # L4
    total_washing_time = total_normal_cars_time + suv_time

    # FA
    answer = total_washing_time
    return answer