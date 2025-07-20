def solve():
    """Index: 5298.
    Returns: the total number of cans of food Carla gave away.
    """
    # L1
    initial_stock = 2000 # currently has stocked up 2000 cans of food
    cans_taken_day1 = 500 # 500 people showed up and took 1 can of food each
    cans_left_day1 = initial_stock - cans_taken_day1

    # L2
    restock_amount_day1 = 1500 # restock 1500 more cans
    cans_after_restock_day1 = cans_left_day1 + restock_amount_day1

    # L3
    people_day2_count = 1000 # 1000 people showed up
    cans_per_person_day2 = 2 # took 2 cans of food each
    cans_taken_day2 = people_day2_count * cans_per_person_day2

    # L4
    cans_left_day2 = cans_after_restock_day1 - cans_taken_day2

    # L5
    restock_amount_day2 = 3000 # restocked again with 3000 cans of food
    cans_after_restock_day2 = cans_left_day2 + restock_amount_day2

    # L6
    total_cans_given_away = cans_taken_day1 + cans_taken_day2

    # FA
    answer = total_cans_given_away
    return answer