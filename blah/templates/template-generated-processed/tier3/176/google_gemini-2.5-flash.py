def solve():
    """Index: 176.
    Returns: the total kilograms of sugar sold every week.
    """
    # L1
    packets_sold_per_week = 20 # 20 packets
    grams_per_packet = 100 # 100 grams of sugar
    total_grams_sold = packets_sold_per_week * grams_per_packet

    # L2
    grams_per_kilogram = 1000 # 1 kilogram is equal to 1000 grams
    total_kilograms_sold = total_grams_sold / grams_per_kilogram

    # FA
    answer = total_kilograms_sold
    return answer