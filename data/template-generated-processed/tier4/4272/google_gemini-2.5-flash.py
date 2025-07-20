def solve():
    """Index: 4272.
    Returns: the weight of one serving of Chicken Surprise in ounces.
    """
    # L1
    chicken_pounds = 4.5 # 4.5 pounds of chicken
    ounces_per_pound = 16 # WK
    chicken_ounces = chicken_pounds * ounces_per_pound

    # L2
    stuffing_ounces = 24 # 24 ounces of stuffing
    total_ounces = chicken_ounces + stuffing_ounces

    # L3
    num_servings = 12 # 12 servings of Chicken Surprise
    ounces_per_serving = total_ounces / num_servings

    # FA
    answer = ounces_per_serving
    return answer