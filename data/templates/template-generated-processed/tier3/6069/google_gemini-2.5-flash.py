def solve():
    """Index: 6069.
    Returns: the time it will take to decorate all the eggs.
    """
    # L1
    mia_eggs_per_hour = 24 # 2 dozen Easter eggs per hour (2 * 12)
    billy_eggs_per_hour = 10 # 10 eggs per hour
    combined_eggs_per_hour = mia_eggs_per_hour + billy_eggs_per_hour

    # L2
    total_eggs_needed = 170 # 170 eggs for the Easter egg hunt
    time_to_decorate = total_eggs_needed / combined_eggs_per_hour

    # FA
    answer = time_to_decorate
    return answer