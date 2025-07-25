def solve():
    """Index: 2982.
    Returns: the cost of each gift.
    """
    # L1
    son_teachers = 3 # Her son has 3 different teachers
    daughter_teachers = 4 # her daughter has 4
    total_teachers = son_teachers + daughter_teachers

    # L2
    total_spent = 70 # spent $70 on gifts
    cost_per_gift = total_spent / total_teachers

    # FA
    answer = cost_per_gift
    return answer