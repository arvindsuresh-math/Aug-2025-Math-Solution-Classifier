def solve():
    """Index: 5314.
    Returns: the number of balls each of the other 2 students removed.
    """
    # L1
    tennis_balls_per_basket = 15 # 15 tennis balls
    soccer_balls_per_basket = 5 # 5 soccer balls
    balls_per_basket = tennis_balls_per_basket + soccer_balls_per_basket

    # L2
    num_baskets = 5 # 5 baskets
    total_initial_balls = num_baskets * balls_per_basket

    # L3
    num_students_group1 = 3 # 3 of them removed 8 balls each
    balls_removed_per_student_group1 = 8 # 8 balls each
    total_balls_removed_group1 = num_students_group1 * balls_removed_per_student_group1

    # L4
    balls_left_after_group1 = total_initial_balls - total_balls_removed_group1

    # L5
    balls_still_in_baskets = 56 # a total of 56 balls are still in the baskets
    total_balls_removed_group2 = balls_left_after_group1 - balls_still_in_baskets

    # L6
    num_students_group2 = 2 # the other 2 removed a certain number of balls each
    balls_removed_per_student_group2 = total_balls_removed_group2 / num_students_group2

    # FA
    answer = balls_removed_per_student_group2
    return answer