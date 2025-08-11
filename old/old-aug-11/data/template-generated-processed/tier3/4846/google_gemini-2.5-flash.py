def solve():
    """Index: 4846.
    Returns: the total number of bacterial cells after 4 hours.
    """
    # L1
    hours = 4 # 4 hours
    minutes_per_hour = 60 # WK
    total_minutes = hours * minutes_per_hour

    # L2
    doubling_time_minutes = 20 # doubling time of 20 minutes
    number_of_doublings = total_minutes / doubling_time_minutes

    # L3
    initial_cells = 1 # 1 single bacterial cell
    doubling_factor = 2 # WK
    final_bacterial_cells = initial_cells * (doubling_factor ** int(number_of_doublings))

    # FA
    answer = final_bacterial_cells
    return answer