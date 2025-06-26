def solve(
    workout_goal: int = 30,  # Shawna's workout goal is 30 situps
    monday_situps: int = 12,  # On Monday, Shawna was only able to do 12 situps
    tuesday_situps: int = 19  # On Tuesday, Shawna was only able to do 19 situps
):
    """Index: 63.
    Returns: the number of situps Shawna needs to do on Wednesday to meet her minimum goal and make up for the ones she didn't do.
    """
    #: L1
    monday_short = workout_goal - monday_situps

    #: L2
    tuesday_short = workout_goal - tuesday_situps

    #: L3
    wednesday_situps = workout_goal + monday_short + tuesday_short

    answer = wednesday_situps  # FINAL ANSWER
    return answer