def solve():
    """Index: 3331.
    Returns: the number of plates Hasan needed to remove from the shipping box.
    """
    # L2
    weight_limit_pounds = 20 # 20 pounds
    ounces_per_pound = 16 # WK
    weight_limit_ounces = weight_limit_pounds * ounces_per_pound

    # L5
    initial_plates = 38 # 38 dinner plates
    plate_weight_ounces = 10 # 10 ounces
    remaining_plates_expression_value = weight_limit_ounces / plate_weight_ounces

    # L7
    plates_removed = initial_plates - remaining_plates_expression_value

    # FA
    answer = plates_removed
    return answer