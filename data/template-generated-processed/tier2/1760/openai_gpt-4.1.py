def solve():
    """Index: 1760.
    Returns: the total number of pounds the two friends combined to lose.
    """
    # L1
    alessia_loss_per_week = 1.5 # Aleesia lost 1.5 pounds each week
    alessia_weeks = 10 # for 10 weeks
    alessia_total_loss = alessia_loss_per_week * alessia_weeks

    # L2
    alexei_loss_per_week = 2.5 # Alexei lost 2.5 pounds each week
    alexei_weeks = 8 # for 8 weeks
    alexei_total_loss = alexei_loss_per_week * alexei_weeks

    # L3
    total_loss = alessia_total_loss + alexei_total_loss

    # FA
    answer = total_loss
    return answer