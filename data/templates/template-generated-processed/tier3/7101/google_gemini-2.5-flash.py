def solve():
    """Index: 7101.
    Returns: the total number of pints of ice cream Alice had on Wednesday.
    """
    # L1
    sunday_pints = 4 # On Sunday Alice bought 4 pints
    monday_multiplier = 3 # three times that number of pints
    monday_pints = sunday_pints * monday_multiplier

    # L2
    tuesday_divisor = 3 # one-third of the number of pints she bought the day before
    tuesday_pints = monday_pints / tuesday_divisor

    # L3
    total_pints_before_return = sunday_pints + monday_pints + tuesday_pints

    # L4
    return_divisor = 2 # half of the pints she bought the day before
    returned_pints = tuesday_pints / return_divisor

    # L5
    final_pints_wednesday = total_pints_before_return - returned_pints

    # FA
    answer = final_pints_wednesday
    return answer