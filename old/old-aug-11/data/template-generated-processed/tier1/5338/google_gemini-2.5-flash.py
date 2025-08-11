def solve():
    """Index: 5338.
    Returns: the total number of pieces of clothing Rick has ironed.
    """
    # L1
    shirts_per_hour = 4 # 4 dress shirts in an hour
    hours_ironing_shirts = 3 # spends 3 hours ironing dress shirts
    total_shirts_ironed = shirts_per_hour * hours_ironing_shirts

    # L2
    pants_per_hour = 3 # 3 dress pants in an hour
    hours_ironing_pants = 5 # 5 hours ironing dress pants
    total_pants_ironed = pants_per_hour * hours_ironing_pants

    # L3
    total_clothing_ironed = total_shirts_ironed + total_pants_ironed

    # FA
    answer = total_clothing_ironed
    return answer