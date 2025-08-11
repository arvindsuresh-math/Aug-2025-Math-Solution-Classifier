def solve():
    """Index: 193.
    Returns: the height of the sunflowers from Packet B in inches.
    """
    # L1 (variable setup for L2)
    packet_a_height = 192 # sunflowers from Packet A were 192 inches tall
    percent_taller = 0.20 # Packet A were 20% taller than Packet B
    # L2
    packet_b_multiplier = 1 + percent_taller
    # L3
    packet_b_height = packet_a_height / packet_b_multiplier
    # FA
    answer = packet_b_height
    return answer