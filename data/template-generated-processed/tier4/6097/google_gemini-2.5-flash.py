def solve():
    """Index: 6097.
    Returns: the number of half-ton bags of food John needs to buy.
    """
    # L1
    feedings_per_day = 2 # feeds each horse twice a day
    food_per_feeding = 20 # feeds them 20 pounds of food at each feeding
    food_per_horse_per_day = feedings_per_day * food_per_feeding

    # L2
    num_horses = 25 # John has 25 horses
    total_food_per_day = food_per_horse_per_day * num_horses

    # L3
    num_days = 60 # in 60 days
    total_food_needed = num_days * total_food_per_day

    # L4
    pounds_per_ton = 2000 # WK
    bag_size_tons = 0.5 # half ton bags of food
    pounds_per_bag = pounds_per_ton * bag_size_tons

    # L5
    num_bags_to_buy = total_food_needed / pounds_per_bag

    # FA
    answer = num_bags_to_buy
    return answer