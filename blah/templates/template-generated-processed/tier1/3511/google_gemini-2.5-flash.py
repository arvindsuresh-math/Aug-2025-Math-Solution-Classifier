def solve():
    """Index: 3511.
    Returns: Victoria's remaining balance after purchases.
    """
    # L1
    num_rice_packets = 2 # bought 2 packets of rice
    price_per_rice_packet = 20 # each at $20
    num_wheat_packets = 3 # 3 packets of wheat flour
    price_per_wheat_packet = 25 # each at $25
    price_per_soda = 150 # 1 soda at $150
    total_spent = num_rice_packets * price_per_rice_packet + num_wheat_packets * price_per_wheat_packet + price_per_soda

    # L2
    initial_balance = 500 # Victoria had $500
    remaining_balance = initial_balance - total_spent

    # FA
    answer = remaining_balance
    return answer