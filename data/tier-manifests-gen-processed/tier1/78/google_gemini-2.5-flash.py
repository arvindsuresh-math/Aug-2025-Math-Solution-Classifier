def solve():
    """Index: 78.
    Returns: the number of cookie slices left.
    """
    # L1
    num_cookie_pies = 3 # 3 birthday cookie pies
    slices_per_pie = 10 # cut into 10 slices
    total_slices = num_cookie_pies * slices_per_pie

    # L2
    num_classmates = 24 # 24 classmates
    manny_count = 1 # Manny...had 1 piece
    teacher_count = 1 # his teacher, Mr. Keith...had 1 piece
    total_people = num_classmates + manny_count + teacher_count

    # L3
    slices_eaten = total_people # all had 1 piece, so slices eaten equals total people
    slices_left = total_slices - slices_eaten

    # FA
    answer = slices_left
    return answer