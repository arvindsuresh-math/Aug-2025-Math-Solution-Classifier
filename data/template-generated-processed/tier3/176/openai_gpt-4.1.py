def solve():
    """Index: 176.
    Returns: the number of kilograms of sugar sold every week.
    """
    # L1
    packets_per_week = 20 # 20 packets of 100 grams
    grams_per_packet = 100 # 100 grams of sugar per packet
    total_grams_per_week = packets_per_week * grams_per_packet

    # L2
    grams_per_kilogram = 1000 # 1 kilogram is equal to 1000 grams
    total_kilograms_per_week = total_grams_per_week / grams_per_kilogram

    # FA
    answer = total_kilograms_per_week
    return answer