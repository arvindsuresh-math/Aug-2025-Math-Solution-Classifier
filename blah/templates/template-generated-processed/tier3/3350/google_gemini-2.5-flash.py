def solve():
    """Index: 3350.
    Returns: the number of weeks it takes Jerry to reach the target soda consumption.
    """
    # L1
    initial_sodas = 48 # he drinks 48 sodas a week
    reduction_factor = 2 # cuts the number of sodas he drinks in half each week
    sodas_after_week_1 = initial_sodas / reduction_factor

    # L2
    sodas_after_week_2 = sodas_after_week_1 / reduction_factor

    # L3
    sodas_after_week_3 = sodas_after_week_2 / reduction_factor
    weeks_taken = 3 # WK
    target_sodas = 6 # to only drink 6 sodas per week

    # FA
    answer = weeks_taken
    return answer