def solve():
    """Index: 863.
    Returns: the number of students who do not like either food.
    """
    # L1
    likes_fries = 15 # 15 students said they like French fries
    likes_both = 6 # 6 students who said they like both French fries and burgers
    likes_fries_only = likes_fries - likes_both

    # L2
    likes_burgers = 10 # 10 said they like burgers
    likes_burgers_only = likes_burgers - likes_both

    # L3
    likes_at_least_one = likes_fries_only + likes_burgers_only + likes_both

    # L4
    total_students = 25 # 25 students
    do_not_like_either = total_students - likes_at_least_one

    # FA
    answer = do_not_like_either
    return answer