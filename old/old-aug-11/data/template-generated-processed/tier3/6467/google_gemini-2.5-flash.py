def solve():
    """Index: 6467.
    Returns: the average temperature for the three cities.
    """
    # L1
    temp_new_york = 80 # The temperature in New York in June 2020 was 80 degrees
    miami_hotter_than_ny = 10 # 10 degrees hotter than the temperature in New York
    temp_miami = temp_new_york + miami_hotter_than_ny

    # L2
    miami_cooler_than_sd = 25 # 25 degrees cooler than the temperature in San Diego
    temp_san_diego = temp_miami + miami_cooler_than_sd

    # L3
    total_temperature = temp_san_diego + temp_miami + temp_new_york

    # L4
    number_of_cities = 3 # three cities
    average_temperature = total_temperature / number_of_cities

    # FA
    answer = average_temperature
    return answer