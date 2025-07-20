def solve():
    """Index: 4761.
    Returns: the number of jellybeans still left in the jar.
    """
    # L1
    normal_class_size = 24 # 24 kids
    sick_children = 2 # 2 children called in sick
    children_present = normal_class_size - sick_children

    # L2
    jellybeans_per_child = 3 # eat 3 jellybeans each
    jellybeans_eaten = children_present * jellybeans_per_child

    # L3
    total_jellybeans_initial = 100 # 100 jellybeans in a glass jar
    jellybeans_remaining = total_jellybeans_initial - jellybeans_eaten

    # FA
    answer = jellybeans_remaining
    return answer