def solve():
    """Index: 7077.
    Returns: the total feet of snow they now have.
    """
    # L1
    inches_per_foot = 12 # WK
    initial_snow_feet = 0.5 # .5 feet of snow on the first day of winter
    initial_snow_inches = inches_per_foot * initial_snow_feet

    # L2
    additional_snow_day2_inches = 8 # an additional 8 inches
    snow_after_day2_inches = initial_snow_inches + additional_snow_day2_inches

    # L3
    melted_snow_inches = 2 # 2 inches of the snow melted
    snow_after_melt_inches = snow_after_day2_inches - melted_snow_inches

    # L4
    multiplier_day5 = 2 # 2 times the amount of snow they received on the first day
    snow_day5_inches = multiplier_day5 * initial_snow_inches

    # L5
    total_snow_inches = snow_after_melt_inches + snow_day5_inches

    # L6
    final_snow_feet = total_snow_inches / inches_per_foot

    # FA
    answer = final_snow_feet
    return answer