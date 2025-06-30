def solve(
    current_weight: int = 97, # A boxer weighs 97 kg
    months_until_fight: int = 4, # at 4 months from a fight
    weight_loss_per_month: int = 3 # He is on a diet that allows him to lose 3 kg per month
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """

    #: L1
    total_weight_loss = weight_loss_per_month * months_until_fight # eval: 12 = 3 * 4

    #: L2
    final_weight = current_weight - total_weight_loss # eval: 85 = 97 - 12

    #: FA
    answer = final_weight # eval: 85 = 85
    return answer # eval: return 85
