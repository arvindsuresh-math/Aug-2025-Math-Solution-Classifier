def solve():
    """Index: 3572.
    Returns: the total number of pieces of clothes Eliza ironed.
    """
    # L1
    hours_blouses = 2 # 2 hours ironing blouses
    minutes_per_hour = 60 # 60 minutes equal 1 hour
    total_minutes_blouses = hours_blouses * minutes_per_hour

    # L2
    time_per_blouse = 15 # a blouse in 15 minutes
    num_blouses = total_minutes_blouses / time_per_blouse

    # L3
    hours_dresses = 3 # 3 hours ironing dresses
    total_minutes_dresses = hours_dresses * minutes_per_hour

    # L4
    time_per_dress = 20 # a dress in 20 minutes
    num_dresses = total_minutes_dresses / time_per_dress

    # L5
    total_pieces_of_clothes = num_blouses + num_dresses

    # FA
    answer = total_pieces_of_clothes
    return answer