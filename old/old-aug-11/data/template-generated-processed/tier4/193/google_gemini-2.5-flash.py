def solve():
    """Index: 193.
    Returns: the height of sunflowers from Packet B.
    """
    # L2
    packet_a_height = 192 # 192 inches tall
    taller_percentage = 0.20 # 20% taller
    base_factor = 1 # WK
    combined_factor = base_factor + taller_percentage

    # L3
    packet_b_height = packet_a_height / combined_factor

    # FA
    answer = packet_b_height
    return answer