def solve():
    """Index: 411.
    Returns: the total number of grandchildren Max has.
    """
    # L1
    max_children = 8 # Max has 8 children
    num_children_with_5 = 2 # except for 2 who have 5 children each
    num_children_with_8 = max_children - num_children_with_5

    # L2
    grandchildren_per_8 = 8 # each of his children has the same number of children as he does
    grandchildren_from_8 = num_children_with_8 * grandchildren_per_8

    # L3
    grandchildren_per_5 = 5 # 2 who have 5 children each
    grandchildren_from_5 = grandchildren_per_5 * num_children_with_5

    # L4
    total_grandchildren = grandchildren_from_8 + grandchildren_from_5

    # FA
    answer = total_grandchildren
    return answer