def solve():
    """Index: 7050.
    Returns: the total number of bricks that he has used.
    """
    # L1
    num_walls = 4 # build 4 such walls
    courses_per_wall = 6 # 6 courses of a wall
    total_courses_planned = num_walls * courses_per_wall

    # L2
    bricks_per_course = 10 # 10 bricks per course
    total_bricks_planned = total_courses_planned * bricks_per_course

    # L3
    courses_not_finished = 2 # won't be able to finish two courses
    bricks_missing = courses_not_finished * bricks_per_course

    # L4
    total_bricks_used = total_bricks_planned - bricks_missing

    # FA
    answer = total_bricks_used
    return answer