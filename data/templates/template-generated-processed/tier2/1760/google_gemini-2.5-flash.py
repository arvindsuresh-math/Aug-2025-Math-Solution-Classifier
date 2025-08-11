def solve():
    """Index: 1760.
    Returns: the total pounds lost by the two friends combined.
    """
    # L1
    alessia_weekly_loss = 1.5 # lost 1.5 pounds each week
    alessia_weeks = 10 # for 10 weeks
    alessia_total_loss = alessia_weekly_loss * alessia_weeks

    # L2
    alexei_weekly_loss = 2.5 # lost 2.5 pounds each week
    alexei_weeks = 8 # for 8 weeks
    alexei_total_loss = alexei_weekly_loss * alexei_weeks

    # L3
    combined_loss = alessia_total_loss + alexei_total_loss

    # FA
    answer = combined_loss
    return answer