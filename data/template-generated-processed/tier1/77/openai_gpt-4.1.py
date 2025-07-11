def solve():
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """
    # L1
    months_until_fight = 4 # 4 months from a fight
    kg_lost_per_month = 3 # lose 3 kg per month
    total_kg_lost = kg_lost_per_month * months_until_fight

    # L2
    initial_weight = 97 # weighs 97 kg
    final_weight = initial_weight - total_kg_lost

    # FA
    answer = final_weight
    return answer