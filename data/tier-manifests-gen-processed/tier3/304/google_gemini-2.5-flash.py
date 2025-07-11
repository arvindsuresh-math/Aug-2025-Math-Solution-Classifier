def solve():
    """Index: 304.
    Returns: the percentage of total water used that will go to Farmer Bob's farm.
    """
    # L1
    corn_water_per_acre = 20 # corn takes 20 gallons of water an acre
    bean_water_multiplier = 2 # beans take twice as much water as corn
    beans_water_per_acre = corn_water_per_acre * bean_water_multiplier

    # L2
    bob_corn_acres = 3 # Farmer Bob grows 3 acres of corn
    bob_cotton_acres = 9 # 9 acres of cotton
    cotton_water_per_acre = 80 # cotton takes 80 gallons of water an acre
    bob_bean_acres = 12 # 12 acres of beans
    bob_total_water = bob_corn_acres * corn_water_per_acre + bob_cotton_acres * cotton_water_per_acre + bob_bean_acres * beans_water_per_acre

    # L3
    brenda_corn_acres = 6 # Farmer Brenda grows 6 acres of corn
    brenda_cotton_acres = 7 # 7 acres of cotton
    brenda_bean_acres = 14 # 14 acres of beans
    brenda_total_water = brenda_corn_acres * corn_water_per_acre + brenda_cotton_acres * cotton_water_per_acre + brenda_bean_acres * beans_water_per_acre

    # L4
    bernie_corn_acres = 2 # Farmer Bernie grows 2 acres of corn
    bernie_cotton_acres = 12 # and 12 acres of cotton
    bernie_total_water = bernie_corn_acres * corn_water_per_acre + bernie_cotton_acres * cotton_water_per_acre

    # L5
    total_water_used = bob_total_water + brenda_total_water + bernie_total_water

    # L6
    percentage_multiplier = 100 # WK
    bob_water_percentage = bob_total_water / total_water_used * percentage_multiplier

    # FA
    answer = bob_water_percentage
    return answer