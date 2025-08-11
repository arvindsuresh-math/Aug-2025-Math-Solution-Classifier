def solve():
    """Index: 3770.
    Returns: the total number of balls Matthias has without holes.
    """
    # L1
    total_soccer_balls = 40 # 40 soccer balls
    holed_soccer_balls = 30 # 30 soccer balls ... have a hole in them
    soccer_balls_no_holes = total_soccer_balls - holed_soccer_balls

    # L2
    total_basketballs = 15 # 15 basketballs
    holed_basketballs = 7 # 7 basketballs have a hole in them
    basketballs_no_holes = total_basketballs - holed_basketballs

    # L3
    total_balls_no_holes = soccer_balls_no_holes + basketballs_no_holes

    # FA
    answer = total_balls_no_holes
    return answer