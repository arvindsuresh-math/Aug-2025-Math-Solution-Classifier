def solve():
    """Index: 3469.
    Returns: the number of hours Wolverine takes doing her workouts in a week.
    """
    # L1
    rayman_hours_per_week = 10 # Rayman does workouts for 10 hours in a week
    multiplier_for_junior = 2 # half the number of hours Junior takes
    junior_hours_per_week = multiplier_for_junior * rayman_hours_per_week

    # L2
    combined_junior_rayman_hours = junior_hours_per_week + rayman_hours_per_week

    # L3
    wolverine_multiplier = 2 # twice the combined total number of hours
    wolverine_hours_per_week = wolverine_multiplier * combined_junior_rayman_hours

    # FA
    answer = wolverine_hours_per_week
    return answer