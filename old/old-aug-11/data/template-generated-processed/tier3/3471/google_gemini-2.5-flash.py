def solve():
    """Index: 3471.
    Returns: the total number of pillows Teddy can make.
    """
    # L1
    five_pounds = 5 # 5 pounds of fluffy foam material
    three_less = 3 # 3 less than 5 pounds
    foam_per_pillow = five_pounds - three_less

    # L2
    pounds_per_ton = 2000 # WK
    num_tons = 3 # three tons of fluffy foam material
    total_pounds_material = pounds_per_ton * num_tons

    # L3
    num_pillows = total_pounds_material / foam_per_pillow

    # FA
    answer = num_pillows
    return answer