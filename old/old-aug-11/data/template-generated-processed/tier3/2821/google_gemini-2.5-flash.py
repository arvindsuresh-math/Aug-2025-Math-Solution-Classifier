def solve():
    """Index: 2821.
    Returns: the number of steaks Matt gets.
    """
    # L1
    beef_pounds = 15 # 15 pounds of beef
    ounces_per_pound = 16 # WK
    total_ounces_of_beef = beef_pounds * ounces_per_pound

    # L2
    steak_weight_ounces = 12 # 12-ounce steaks
    number_of_steaks = total_ounces_of_beef / steak_weight_ounces

    # FA
    answer = number_of_steaks
    return answer