def solve():
    """Index: 6979.
    Returns: the length of the red bus visible to the yellow bus driver.
    """
    # L1
    red_bus_length = 48 # red bus is 48 feet long
    red_bus_orange_car_ratio = 4 # four times the length of an orange car
    orange_car_length = red_bus_length / red_bus_orange_car_ratio

    # L2
    orange_car_yellow_bus_ratio = 3.5 # 3.5 times shorter than the length of a yellow bus
    yellow_bus_length = orange_car_yellow_bus_ratio * orange_car_length

    # L3
    visible_red_bus_length = red_bus_length - yellow_bus_length

    # FA
    answer = visible_red_bus_length
    return answer