def solve():
    """Index: 6063.
    Returns: the total number of people Megan can feed.
    """
    # L1
    hours_available = 2 # She spends 2 hours preparing
    minutes_per_hour = 60 # WK
    total_minutes_available = hours_available * minutes_per_hour

    # L2
    prep_time_per_dish = 20 # 20 minutes preparing one dish
    num_dishes_made = total_minutes_available / prep_time_per_dish

    # L3
    people_per_dish = 5 # Each dish can feed 5 people
    total_people_fed = people_per_dish * num_dishes_made

    # FA
    answer = total_people_fed
    return answer