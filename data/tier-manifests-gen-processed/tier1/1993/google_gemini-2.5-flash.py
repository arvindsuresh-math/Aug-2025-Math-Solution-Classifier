def solve():
    """Index: 1993.
    Returns: the total number of times they have coughed after a given duration.
    """
    # L1
    georgia_coughs_per_minute = 5 # coughs 5 times a minute
    robert_multiplier = 2 # coughs twice as much as her
    robert_coughs_per_minute = robert_multiplier * georgia_coughs_per_minute

    # L2
    combined_coughs_per_minute = georgia_coughs_per_minute + robert_coughs_per_minute

    # L3
    time_minutes = 20 # After 20 minutes
    total_coughs = combined_coughs_per_minute * time_minutes

    # FA
    answer = total_coughs
    return answer