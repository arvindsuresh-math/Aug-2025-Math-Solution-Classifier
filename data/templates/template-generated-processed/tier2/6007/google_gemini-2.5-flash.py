def solve():
    """Index: 6007.
    Returns: the total amount Harry will spend on seeds.
    """
    # L1
    num_pumpkin_packets = 3 # three packets of pumpkin seeds
    cost_per_pumpkin_packet = 2.50 # $2.50
    cost_pumpkin_seeds = num_pumpkin_packets * cost_per_pumpkin_packet

    # L2
    num_tomato_packets = 4 # four packets of tomato seeds
    cost_per_tomato_packet = 1.50 # $1.50
    cost_tomato_seeds = num_tomato_packets * cost_per_tomato_packet

    # L3
    num_chili_pepper_packets = 5 # five packets of chili pepper seeds
    cost_per_chili_pepper_packet = 0.90 # $0.90
    cost_chili_pepper_seeds = num_chili_pepper_packets * cost_per_chili_pepper_packet
    total_spend = cost_pumpkin_seeds + cost_tomato_seeds + cost_chili_pepper_seeds

    # FA
    answer = total_spend
    return answer