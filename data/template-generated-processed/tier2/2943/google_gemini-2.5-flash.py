def solve():
    """Index: 2943.
    Returns: the final temperature after all changes.
    """
    # L1
    initial_temperature = 40 # thermostat set to 40 degrees
    double_factor = 2 # WK
    temp_after_double = initial_temperature * double_factor

    # L2
    dad_reduction_amount = 30 # reducing the temperature by 30 degrees
    temp_after_dad_reduction = temp_after_double - dad_reduction_amount

    # L3
    mother_reduction_decimal = 0.3 # by 30%
    mother_reduction_amount = temp_after_dad_reduction * mother_reduction_decimal

    # L4
    temp_after_mother_reduction = temp_after_dad_reduction - mother_reduction_amount

    # L5
    sister_increase_amount = 24 # increases it by 24 degrees
    final_temperature = temp_after_mother_reduction + sister_increase_amount

    # FA
    answer = final_temperature
    return answer