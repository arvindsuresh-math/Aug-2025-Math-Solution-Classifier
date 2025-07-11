def solve():
    """Index: 863.
    Returns: the number of students who do not like either French fries or burgers.
    """
    # L1
    fries_likers = 15 # 15 students said they like French fries
    both_likers = 6 # 6 students who said they like both French fries and burgers
    fries_only = fries_likers - both_likers

    # L2
    burger_likers = 10 # 10 said they like burgers
    burgers_only = burger_likers - both_likers

    # L3
    total_likers = fries_only + burgers_only + both_likers

    # L4
    total_students = 25 # In a class of 25 students
    neither = total_students - total_likers

    # FA
    answer = neither
    return answer