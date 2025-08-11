def solve():
    """Index: 4787.
    Returns: the number of days it takes Marla to collect enough bottle caps to buy a horse.
    """
    # L1
    lizards_per_gallons_num = 3 # 3 lizards are worth 5 gallons of water
    lizards_per_gallons_den = 5 # 3 lizards are worth 5 gallons of water
    lizards_per_gallon = lizards_per_gallons_num / lizards_per_gallons_den

    # L2
    gallons_for_horse = 80 # 1 horse is worth 80 gallons of water
    lizards_for_horse = gallons_for_horse * lizards_per_gallon

    # L3
    bottle_caps_per_lizard = 8 # 1 lizard is worth 8 bottle caps
    bottle_caps_for_horse = lizards_for_horse * bottle_caps_per_lizard

    # L4
    daily_scavenge_caps = 20 # scavenge for 20 bottle caps each day
    daily_food_shelter_cost = 4 # pay 4 bottle caps per night for food and shelter
    daily_net_caps = daily_scavenge_caps - daily_food_shelter_cost

    # L5
    days_to_collect = bottle_caps_for_horse / daily_net_caps

    # FA
    answer = days_to_collect
    return answer