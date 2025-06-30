def solve(
    initial_weight: float = 97,  # boxer weighs 97 kg at 4 months from a fight
    months_to_fight: int = 4,  # 4 months from the fight
    weight_loss_per_month: float = 3  # loses 3 kg per month
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight."""
    #: L1
    total_weight_loss = weight_loss_per_month * months_to_fight

    #: L2
    final_weight = initial_weight - total_weight_loss

    answer = final_weight  # FINAL ANSWER
    return answer