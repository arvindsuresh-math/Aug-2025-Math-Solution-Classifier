def solve():
    """Index: 2479.
    Returns: the number of packets of corn chips John could buy.
    """
    # L1
    num_chips_packets = 15 # 15 packets of chips
    cost_per_chip_packet = 2 # $2 per packet
    cost_chips = num_chips_packets * cost_per_chip_packet

    # L2
    total_money = 45 # $45 for his entire purchase
    money_left = total_money - cost_chips

    # L3
    cost_per_corn_chip_packet = 1.5 # $1.5 per packet
    num_corn_chips_packets = money_left / cost_per_corn_chip_packet

    # FA
    answer = num_corn_chips_packets
    return answer