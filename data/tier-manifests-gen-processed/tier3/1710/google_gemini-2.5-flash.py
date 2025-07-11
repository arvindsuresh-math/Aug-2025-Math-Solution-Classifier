def solve():
    """Index: 1710.
    Returns: the average temperature for July 4th in Washington, DC over the past 5 years.
    """
    # L1
    temp_2020 = 90 # 90 degrees in 2020
    temp_2019 = 90 # 90 degrees in 2019
    temp_2018 = 90 # 90 degrees in 2018
    temp_2017 = 79 # 79 degrees in 2017
    temp_2016 = 71 # 71 degrees in 2016
    sum_of_temperatures = temp_2020 + temp_2019 + temp_2018 + temp_2017 + temp_2016

    # L2
    number_of_years = 5 # past five years
    average_temperature = sum_of_temperatures / number_of_years

    # FA
    answer = average_temperature
    return answer