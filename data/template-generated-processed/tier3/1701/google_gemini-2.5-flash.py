def solve():
    """Index: 1701.
    Returns: the number of pies Sandra can make.
    """
    # L1
    total_weight = 120 # weighs 120 pounds
    applesauce_divisor = 2 # half the weight
    applesauce_weight = total_weight / applesauce_divisor

    # L2
    remaining_apples_for_pies = total_weight - applesauce_weight

    # L3
    pounds_per_pie = 4 # needs 4 pounds of apples per pie
    num_pies = remaining_apples_for_pies / pounds_per_pie

    # FA
    answer = num_pies
    return answer