def solve():
    """Index: 2716.
    Returns: Sam's current age.
    """
    # L1
    drew_current_age = 12 # Drew is currently 12 years old
    years_in_future = 5 # In five years
    drew_age_in_five_years = drew_current_age + years_in_future

    # L2
    sam_age_multiplier = 3 # 3 times as old as Drew
    sam_age_in_five_years = sam_age_multiplier * drew_age_in_five_years

    # L3
    sam_current_age = sam_age_in_five_years - years_in_future

    # FA
    answer = sam_current_age
    return answer