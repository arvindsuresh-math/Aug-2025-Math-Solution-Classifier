def solve():
    """Index: 6760.
    Returns: the total number of hotdogs Matthew needs to cook.
    """
    # L1
    ella_hotdogs = 2 # 2 hotdogs each
    emma_hotdogs = 2 # 2 hotdogs each
    sisters_total_hotdogs = ella_hotdogs + emma_hotdogs

    # L2
    luke_multiplier = 2 # twice the amount of hotdogs as his sisters
    hotdogs_per_sister_for_luke_calc = 2 # 2 hotdogs each
    luke_hotdogs = luke_multiplier * hotdogs_per_sister_for_luke_calc

    # L3
    hunter_multiplier = 1.5 # 1 and half times the total amount of his sisters
    hunter_hotdogs = hunter_multiplier * sisters_total_hotdogs

    # L4
    total_hotdogs = sisters_total_hotdogs + luke_hotdogs + hunter_hotdogs

    # FA
    answer = total_hotdogs
    return answer