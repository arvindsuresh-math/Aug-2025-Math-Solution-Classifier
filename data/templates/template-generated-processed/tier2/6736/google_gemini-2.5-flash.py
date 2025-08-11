def solve():
    """Index: 6736.
    Returns: the total money Georgia would spend on carnations.
    """
    # L1
    dozen_carnation_price = 4.00 # one dozen carnations for $4.00
    num_teachers = 5 # 5 teachers
    cost_for_teachers = dozen_carnation_price * num_teachers

    # L2
    num_friends = 14 # 14 friends
    carnations_per_dozen = 12 # WK
    remaining_single_carnations = num_friends - carnations_per_dozen

    # L3
    cost_per_single_carnation = 0.50 # $0.50
    cost_for_single_carnations = remaining_single_carnations * cost_per_single_carnation

    # L4
    total_money_spent = cost_for_teachers + dozen_carnation_price + cost_for_single_carnations

    # FA
    answer = total_money_spent
    return answer