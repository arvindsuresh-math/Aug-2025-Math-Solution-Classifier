def solve():
    """Index: 4209.
    Returns: the amount of butter needed for the reduced recipe.
    """
    # L1
    original_dozens = 16 # makes 16 dozen cookies
    desired_dozens = 4 # make 4 dozen cookies
    reduction_factor = original_dozens / desired_dozens

    # L2
    original_butter_pounds = 4 # calls for 4 pounds of butter
    butter_needed = original_butter_pounds / reduction_factor

    # FA
    answer = butter_needed
    return answer