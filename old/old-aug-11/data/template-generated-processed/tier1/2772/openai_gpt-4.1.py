def solve():
    """Index: 2772.
    Returns: the total number of plants Shyne can grow in her backyard.
    """
    # L1
    eggplants_per_packet = 14 # 14 eggplants in every seed packet
    eggplant_packets = 4 # 4 seed packets of eggplants
    total_eggplants = eggplants_per_packet * eggplant_packets

    # L2
    sunflowers_per_packet = 10 # 10 sunflowers in every seed packet
    sunflower_packets = 6 # 6 seed packets of sunflower
    total_sunflowers = sunflowers_per_packet * sunflower_packets

    # L3
    total_plants = total_eggplants + total_sunflowers

    # FA
    answer = total_plants
    return answer