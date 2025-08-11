def solve():
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """
    # L1
    weight_loss_per_month = 3 # lose 3 kg per month
    months_until_fight = 4 # 4 months from a fight
    total_weight_loss = weight_loss_per_month * months_until_fight

    # L2
    initial_weight = 97 # weighs 97 kg
    final_weight = initial_weight - total_weight_loss

    # FA
    answer = final_weight
    return answer