def solve(
        daily_goal: int = 30,  # Shawna's workout goal is 30 situps
        monday_situps: int = 12,  # On Monday, Shawna was only able to do 12 situps
        tuesday_situps: int = 19  # she was only able to do 19 situps on Tuesday
):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her goal.
    """

    #: L1
    monday_shortfall = daily_goal - monday_situps

    #: L2
    tuesday_shortfall = daily_goal - tuesday_situps

    #: L3
    wednesday_situps = daily_goal + monday_shortfall + tuesday_shortfall

    #: FA
    answer = wednesday_situps
    return answer