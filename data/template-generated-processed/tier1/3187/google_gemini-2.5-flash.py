def solve():
    """Index: 3187.
    Returns: the total number of sun salutations Summer performs in a year.
    """
    # L1
    poses_per_weekday = 5 # 5 sun salutation yoga poses
    weekdays_per_week = 5 # WK
    salutations_per_week = poses_per_weekday * weekdays_per_week

    # L2
    weeks_per_year = 52 # WK
    total_salutations_per_year = weeks_per_year * salutations_per_week

    # FA
    answer = total_salutations_per_year
    return answer