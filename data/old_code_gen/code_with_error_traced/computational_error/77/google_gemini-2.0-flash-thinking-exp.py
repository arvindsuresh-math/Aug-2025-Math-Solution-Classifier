def solve(
    initial_weight: int = 97, # A boxer weighs 97 kg
    months_until_fight: int = 4, # at 4 months from a fight
    weight_loss_per_month: int = 3 # lose 3 kg per month
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """

    #: L1
    total_weight_loss = 2 # eval: 2 = 2

    #: L2
    final_weight = initial_weight - total_weight_loss # eval: 95 = 97 - 2

    #: FA
    answer = final_weight
    return answer # eval: return 95
