def solve():
    """Index: 3789.
    Returns: the total number of widgets shipped in each shipping box.
    """
    # L1
    carton_width = 4 # 4 inches wide
    carton_length = 4 # 4 inches long
    carton_height = 5 # 5 inches tall
    carton_volume = carton_width * carton_length * carton_height

    # L2
    box_width = 20 # 20 inches wide
    box_length = 20 # 20 inches long
    box_height = 20 # 20 inches high
    box_volume = box_width * box_length * box_height

    # L3
    num_cartons_per_box = box_volume / carton_volume

    # L4
    widgets_per_carton = 3 # 3 widgets in each carton
    total_widgets_per_box = widgets_per_carton * num_cartons_per_box

    # FA
    answer = total_widgets_per_box
    return answer