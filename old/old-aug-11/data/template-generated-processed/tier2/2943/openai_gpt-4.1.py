def solve():
    """Index: 2943.
    Returns: the final temperature after all changes.
    """
    # L1
    initial_temp = 40 # thermostat set to 40 degrees
    double_factor = 2 # double the initial temperature
    temp_after_jerry = initial_temp * double_factor

    # L2
    dad_reduction = 30 # reducing the temperature by 30 degrees
    temp_after_dad = temp_after_jerry - dad_reduction

    # L3
    mom_reduction_percent = 0.3 # reduces the temperature by 30%
    mom_reduction_amount = temp_after_dad * mom_reduction_percent

    # L4
    temp_after_mom = temp_after_dad - mom_reduction_amount

    # L5
    sister_increase = 24 # increases it by 24 degrees
    final_temp = temp_after_mom + sister_increase

    # FA
    answer = final_temp
    return answer