def solve():
    """Index: 411.
    Returns: the total number of grandchildren Max has.
    """
    # L1
    max_children = 8 # Max has 8 children
    children_with_different_num_grandchildren = 2 # 2 who have 5 children each
    children_with_same_num_grandchildren = max_children - children_with_different_num_grandchildren

    # L2
    grandchildren_per_same_child = 8 # children as he does (8)
    grandchildren_from_same_children = children_with_same_num_grandchildren * grandchildren_per_same_child

    # L3
    grandchildren_per_different_child = 5 # 5 children each
    grandchildren_from_different_children = grandchildren_per_different_child * children_with_different_num_grandchildren

    # L4
    total_grandchildren = grandchildren_from_same_children + grandchildren_from_different_children

    # FA
    answer = total_grandchildren
    return answer