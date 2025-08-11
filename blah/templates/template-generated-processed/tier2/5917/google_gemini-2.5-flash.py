def solve():
    """Index: 5917.
    Returns: the final number of dogs Harly has.
    """
    # L1
    total_dogs = 80 # 80 dogs
    adopted_percent_num = 40 # 40%
    percent_factor = 0.01 # WK
    dogs_adopted_out = total_dogs * adopted_percent_num * percent_factor

    # L2
    returned_dogs = 5 # take back 5
    final_dogs = total_dogs - dogs_adopted_out + returned_dogs

    # FA
    answer = final_dogs
    return answer