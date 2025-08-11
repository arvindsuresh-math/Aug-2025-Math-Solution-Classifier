def solve():
    """Index: 4075.
    Returns: the combined ages of Richard and Hurley 40 years from now.
    """
    # L1
    hurley_current_age = 14 # Hurley is 14 years old
    age_difference = 20 # difference in ages between Richard and Hurley is 20
    richard_current_age = age_difference + hurley_current_age

    # L2
    years_from_now = 40 # 40 years from now
    hurley_future_age = hurley_current_age + years_from_now

    # L3
    richard_future_age = years_from_now + richard_current_age

    # L4
    combined_future_ages = richard_future_age + hurley_future_age

    # FA
    answer = combined_future_ages
    return answer