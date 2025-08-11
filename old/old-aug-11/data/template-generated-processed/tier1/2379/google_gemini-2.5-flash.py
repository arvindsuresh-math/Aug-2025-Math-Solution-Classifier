def solve():
    """Index: 2379.
    Returns: the total gallons of water Carla needs to bring.
    """
    # L1
    num_pigs = 8 # 8 pigs
    pig_water_needed_per_pig = 3 # each pig needs 3 gallons of water
    total_pig_water = num_pigs * pig_water_needed_per_pig

    # L2
    horse_water_multiplier_from_pig = 2 # twice as much water as a pig
    water_per_horse = pig_water_needed_per_pig * horse_water_multiplier_from_pig

    # L3
    num_horses = 10 # 10 horses
    total_horse_water = num_horses * water_per_horse

    # L4
    chicken_tank_gallons = 30 # one tank that needs 30 gallons
    total_water_needed = total_pig_water + total_horse_water + chicken_tank_gallons

    # FA
    answer = total_water_needed
    return answer