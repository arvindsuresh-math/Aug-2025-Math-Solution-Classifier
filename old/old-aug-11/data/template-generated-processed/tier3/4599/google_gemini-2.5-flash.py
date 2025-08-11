def solve():
    """Index: 4599.
    Returns: the total ounces of milk bought by the shopkeeper.
    """
    # L1
    num_packets = 150 # 150 packets of milk
    ml_per_packet = 250 # 250 ml of milk
    total_ml_milk = ml_per_packet * num_packets

    # L2
    ml_per_ounce = 30 # one fluid ounce is equal to 30 ml
    total_oz_milk = total_ml_milk / ml_per_ounce

    # FA
    answer = total_oz_milk
    return answer