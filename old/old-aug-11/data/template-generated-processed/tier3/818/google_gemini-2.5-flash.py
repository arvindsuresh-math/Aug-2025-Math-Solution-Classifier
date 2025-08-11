def solve():
    """Index: 818.
    Returns: the total number of hours it will take to complete Trey's list.
    """
    # L1
    clean_house_items = 7 # 7 things to do to clean the house
    shower_items = 1 # 1 thing to do to take a shower
    dinner_items = 4 # 4 things to do to make dinner
    total_items = clean_house_items + shower_items + dinner_items

    # L2
    time_per_item_minutes = 10 # takes 10 minutes to do
    total_minutes = time_per_item_minutes * total_items

    # L3
    minutes_per_hour = 60 # WK
    total_hours = total_minutes / minutes_per_hour

    # FA
    answer = total_hours
    return answer