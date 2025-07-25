def solve():
    """Index: 7418.
    Returns: the total number of bottle caps in Josh's collection.
    """
    # L1
    collection_weight_pounds = 18 # 18 pounds exactly
    ounces_per_pound = 16 # WK
    collection_weight_ounces = collection_weight_pounds * ounces_per_pound

    # L2
    caps_per_ounce = 7 # 7 bottle caps weigh exactly one ounce
    total_caps = collection_weight_ounces * caps_per_ounce

    # FA
    answer = total_caps
    return answer