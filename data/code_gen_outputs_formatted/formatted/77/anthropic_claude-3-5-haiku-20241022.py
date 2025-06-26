def solve(
    initial_weight: float = 97,  # boxer weighs 97 kg at 4 months from a fight
    weight_loss_per_month: float = 3,  # he loses 3 kg per month
    months_until_fight: int = 4  # 4 months from the fight
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight."""

    #: L1
    total_weight_loss = weight_loss_per_month * months_until_fight

    answer = initial_weight - total_weight_loss  # FINAL ANSWER
    return answer