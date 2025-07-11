def solve():
    """Index: 2379.
    Returns: the total gallons of water Carla needs to bring for all her animals.
    """
    # L1
    num_pigs = 8 # she has 8 pigs
    pig_gallons = 3 # each pig needs 3 gallons of water
    total_pig_gallons = num_pigs * pig_gallons

    # L2
    horse_multiplier = 2 # each horse needs twice as much water as a pig
    horse_gallons = pig_gallons * horse_multiplier

    # L3
    num_horses = 10 # she has 10 horses
    total_horse_gallons = num_horses * horse_gallons

    # L4
    chicken_tank_gallons = 30 # the chickens drink from one tank that needs 30 gallons
    total_gallons = total_pig_gallons + total_horse_gallons + chicken_tank_gallons

    # FA
    answer = total_gallons
    return answer