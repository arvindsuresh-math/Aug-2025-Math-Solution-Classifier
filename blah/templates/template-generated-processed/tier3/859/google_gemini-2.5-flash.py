def solve():
    """Index: 859.
    Returns: the time in minutes to fill the target number of packets.
    """
    # L1
    gummy_bears_per_minute = 300 # manufactures 300 gummy bears a minute
    gummy_bears_per_packet = 50 # Each packet of gummy bears has 50 gummy bears inside
    packets_per_minute = gummy_bears_per_minute / gummy_bears_per_packet

    # L2
    target_packets = 240 # fill 240 packets
    time_in_minutes = target_packets / packets_per_minute

    # FA
    answer = time_in_minutes
    return answer