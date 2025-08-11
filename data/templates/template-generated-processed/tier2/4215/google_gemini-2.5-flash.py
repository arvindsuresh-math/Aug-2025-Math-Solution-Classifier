def solve():
    """Index: 4215.
    Returns: the total time spent on all pictures.
    """
    # L1
    drawing_time_per_picture = 2 # 2 hours to draw each picture
    time_reduction_percent = 0.3 # 30% less time
    coloring_time_reduction = drawing_time_per_picture * time_reduction_percent

    # L2
    actual_coloring_time_per_picture = drawing_time_per_picture - coloring_time_reduction

    # L3
    total_time_per_picture = drawing_time_per_picture + actual_coloring_time_per_picture

    # L4
    num_pictures = 10 # 10 pictures
    total_time_all_pictures = total_time_per_picture * num_pictures

    # FA
    answer = total_time_all_pictures
    return answer