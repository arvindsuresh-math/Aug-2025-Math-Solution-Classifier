def solve():
    """Index: 4220.
    Returns: the total number of sticks of gum in 8 brown boxes.
    """
    # L1
    packs_per_carton = 5 # Each carton contains 5 packs of gum
    sticks_per_pack = 3 # 3 sticks of gum in each pack
    sticks_per_carton = packs_per_carton * sticks_per_pack

    # L2
    cartons_per_brown_box = 4 # Each brown box contains 4 cartons of gum
    num_brown_boxes = 8 # 8 brown boxes
    total_cartons = num_brown_boxes * cartons_per_brown_box

    # L3
    total_sticks = total_cartons * sticks_per_carton

    # FA
    answer = total_sticks
    return answer