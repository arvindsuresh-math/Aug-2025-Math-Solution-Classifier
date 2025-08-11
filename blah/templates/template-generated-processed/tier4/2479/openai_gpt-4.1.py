def solve():
    """Index: 2479.
    Returns: the number of packets of corn chips John could buy.
    """
    # L1
    num_chips_packets = 15 # John would like to buy 15 packets of chips
    chips_price_per_packet = 2 # chips for $2 per packet
    chips_total_cost = num_chips_packets * chips_price_per_packet

    # L2
    john_total_money = 45 # John has $45 for his entire purchase
    money_left = john_total_money - chips_total_cost

    # L3
    corn_chips_price_per_packet = 1.5 # corn chips for $1.5 per packet
    corn_chips_packets = money_left / corn_chips_price_per_packet

    # FA
    answer = corn_chips_packets
    return answer