def solve():
    """Index: 4215.
    Returns: the total time John spends on all the pictures.
    """
    # L1
    draw_time_per_pic = 2 # 2 hours to draw each picture
    coloring_time_reduction_percent = 0.3 # 30% less time
    coloring_time_saved = draw_time_per_pic * coloring_time_reduction_percent

    # L2
    color_time_per_pic = draw_time_per_pic - coloring_time_saved

    # L3
    total_time_per_pic = draw_time_per_pic + color_time_per_pic

    # L4
    num_pictures = 10 # 10 pictures
    total_time_all_pics = total_time_per_pic * num_pictures

    # FA
    answer = total_time_all_pics
    return answer