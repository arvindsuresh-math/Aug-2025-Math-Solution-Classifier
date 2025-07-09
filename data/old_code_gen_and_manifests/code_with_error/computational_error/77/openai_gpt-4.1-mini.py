def solve(
    current_weight: int = 97,  # A boxer weighs 97 kg at 4 months from a fight
    months_until_fight: int = 4,  # 4 months from a fight
    weight_loss_per_month: int = 3  # He is on a diet that allows him to lose 3 kg per month
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """

    #: L1
    total_weight_loss = weight_loss_per_month * months_until_fight

    #: L2
    weight_on_fight_day = 95

    #: FA
    answer = weight_on_fight_day
    return answer