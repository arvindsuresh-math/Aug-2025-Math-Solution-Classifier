def solve(
    current_weight: int = 97,  # A boxer weighs 97 kg at 4 months from a fight
    months_until_fight: int = 4,  # 4 months from a fight
    weight_loss_per_month: int = 3  # He is on a diet that allows him to lose 3 kg per month
):
    """Index: 77.
    Returns: the boxer's weight on the day of the fight.
    """

    #: L1

    #: L2
    weight_on_fight_day = current_weight - months_until_fight

    #: FA
    answer = weight_on_fight_day
    return answer