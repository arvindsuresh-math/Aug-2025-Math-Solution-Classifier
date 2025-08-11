def solve():
    """Index: 4762.
    Returns: the weight difference in pounds between the heavier and lighter TV.
    """
    # L1
    bill_tv_width = 48 # 48 inches
    bill_tv_length = 100 # 100 inches
    bill_tv_area = bill_tv_width * bill_tv_length

    # L2
    bob_tv_width = 70 # 70 inches
    bob_tv_length = 60 # 60 inches
    bob_tv_area = bob_tv_width * bob_tv_length

    # L3
    area_difference = bill_tv_area - bob_tv_area

    # L4
    weight_per_sq_inch = 4 # 4 oz per square inch
    weight_difference_oz = area_difference * weight_per_sq_inch

    # L5
    ounces_per_pound = 16 # There are 16 ounces per pound
    weight_difference_pounds = weight_difference_oz / ounces_per_pound

    # FA
    answer = weight_difference_pounds
    return answer