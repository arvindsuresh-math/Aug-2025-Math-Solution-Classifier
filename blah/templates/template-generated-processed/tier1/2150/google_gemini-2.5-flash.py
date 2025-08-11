def solve():
    """Index: 2150.
    Returns: the number of eggs not being eaten every week.
    """
    # L1
    eggs_per_tray = 24 # If each tray has 24 eggs
    trays_per_week = 2 # 2 trays of eggs every week
    total_eggs_bought_per_week = eggs_per_tray * trays_per_week

    # L2
    son_daughter_eggs_per_morning = 2 # son and daughter eat 2 eggs every morning
    days_per_week = 7 # WK
    son_daughter_eggs_eaten_per_week = son_daughter_eggs_per_morning * days_per_week

    # L3
    rhea_husband_eggs_per_night = 4 # Rhea and her husband eat 4 eggs every night
    rhea_husband_eggs_eaten_per_week = rhea_husband_eggs_per_night * days_per_week

    # L4
    total_eggs_eaten_per_week = rhea_husband_eggs_eaten_per_week + son_daughter_eggs_eaten_per_week

    # L5
    eggs_not_eaten = total_eggs_bought_per_week - total_eggs_eaten_per_week

    # FA
    answer = eggs_not_eaten
    return answer