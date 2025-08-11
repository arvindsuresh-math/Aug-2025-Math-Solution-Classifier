def solve():
    """Index: 4314.
    Returns: the number of pieces of laundry Carla needs to clean per hour.
    """
    # L1
    end_time = 12 # by noon
    start_time = 8 # at 8 AM
    hours_to_work = end_time - start_time

    # L2
    total_laundry_pieces = 80 # 80 pieces of laundry
    pieces_per_hour = total_laundry_pieces / hours_to_work

    # FA
    answer = pieces_per_hour
    return answer