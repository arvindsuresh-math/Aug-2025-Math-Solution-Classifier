def solve():
    """Index: 3393.
    Returns: the total ounces of fudge eaten by the three friends.
    """
    # L1
    tomas_fudge_pounds = 1.5 # 1.5 pounds of chocolate fudge
    ounces_per_pound = 16 # WK
    tomas_fudge_ounces = tomas_fudge_pounds * ounces_per_pound

    # L2
    katya_fudge_pounds = 0.5 # half a pound of peanut butter fudge
    katya_fudge_ounces = katya_fudge_pounds * ounces_per_pound

    # L3
    boris_fudge_pounds = 2 # 2 pounds of fudge
    boris_fudge_ounces = boris_fudge_pounds * ounces_per_pound

    # L4
    total_fudge_ounces = tomas_fudge_ounces + katya_fudge_ounces + boris_fudge_ounces

    # FA
    answer = total_fudge_ounces
    return answer