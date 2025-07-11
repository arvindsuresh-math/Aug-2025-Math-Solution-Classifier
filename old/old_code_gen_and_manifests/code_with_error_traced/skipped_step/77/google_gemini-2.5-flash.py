def solve(
        initial_weight_kg: int = 97, # weighs 97 kg
        months_to_fight: int = 4, # at 4 months from a fight
        weight_loss_per_month_kg: int = 3 # lose 3 kg per month
    ):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """

    #: L1
    total_weight_loss_kg = weight_loss_per_month_kg * months_to_fight # eval: 12 = 3 * 4

    #: L2

    #: FA
    answer = months_to_fight
    return answer # eval: return 4
