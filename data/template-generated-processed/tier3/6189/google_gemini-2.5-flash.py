def solve():
    """Index: 6189.
    Returns: the average temperature in Fahrenheit.
    """
    # L1
    temp1 = -36 # -36 degrees Fahrenheit
    temp2 = 13 # +13 degrees Fahrenheit
    temp3 = -15 # -15 degrees Fahrenheit
    temp4 = -10 # -10 degrees Fahrenheit
    sum_of_temperatures = temp1 + temp2 + temp3 + temp4

    # L2
    number_of_days = 4 # 4 days recorded
    average_temperature = sum_of_temperatures / number_of_days

    # FA
    answer = average_temperature
    return answer