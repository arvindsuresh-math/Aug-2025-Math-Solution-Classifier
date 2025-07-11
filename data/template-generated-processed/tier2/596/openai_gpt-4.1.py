def solve():
    """Index: 596.
    Returns: the total number of minutes the 3 people worked in total.
    """
    # L1
    bianca_hours = 12.5 # Bianca worked for 12.5 hours

    # L2
    celeste_multiplier = 2 # Celeste worked for twice that amount
    celeste_hours = celeste_multiplier * bianca_hours

    # L3
    mcclain_less_hours = 8.5 # McClain worked 8.5 hours less
    mcclain_hours = celeste_hours - mcclain_less_hours

    # L4
    total_hours = bianca_hours + celeste_hours + mcclain_hours

    # L5
    minutes_per_hour = 60 # WK
    total_minutes = total_hours * minutes_per_hour

    # FA
    answer = total_minutes
    return answer