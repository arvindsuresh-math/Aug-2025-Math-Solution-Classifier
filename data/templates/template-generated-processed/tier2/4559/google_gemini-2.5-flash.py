def solve():
    """Index: 4559.
    Returns: how many more ounces of fudge Marina had than Lazlo.
    """
    # L1
    marina_pounds = 4.5 # 4.5 pounds of fudge
    ounces_per_pound = 16 # WK
    marina_ounces = marina_pounds * ounces_per_pound

    # L2
    lazlo_pounds = 4 # 4 pounds of fudge
    lazlo_less_ounces = 6 # 6 ounces less
    lazlo_ounces = (lazlo_pounds * ounces_per_pound) - lazlo_less_ounces

    # L3
    difference_ounces = marina_ounces - lazlo_ounces

    # FA
    answer = difference_ounces
    return answer