def solve():
    """Index: 2206.
    Returns: the total number of vegetables Shanna had to harvest.
    """
    # L1
    initial_tomato_plants = 6 # 6 tomato plants
    tomato_plants_died_divisor = 2 # Half of her tomato plants
    surviving_tomato_plants = initial_tomato_plants / tomato_plants_died_divisor

    # L2
    initial_pepper_plants = 4 # 4 pepper plants
    pepper_plants_died = 1 # one pepper plant died
    surviving_pepper_plants = initial_pepper_plants - pepper_plants_died

    # L3
    eggplant_plants = 2 # 2 eggplant plants
    total_surviving_plants = surviving_tomato_plants + surviving_pepper_plants + eggplant_plants

    # L4
    vegetables_per_plant = 7 # Each gave her 7 vegetables
    total_vegetables_harvested = total_surviving_plants * vegetables_per_plant

    # FA
    answer = total_vegetables_harvested
    return answer