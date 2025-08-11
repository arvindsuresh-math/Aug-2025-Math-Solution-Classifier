def solve():
    """Index: 3921.
    Returns: the average number of branches per foot for the trees.
    """
    # L1
    first_tree_branches = 200 # 200 branches
    first_tree_height = 50 # 50 feet tall
    first_tree_bpf = first_tree_branches / first_tree_height

    # L2
    second_tree_branches = 180 # 180 branches
    second_tree_height = 40 # 40 feet tall
    second_tree_bpf = second_tree_branches / second_tree_height

    # L3
    third_tree_branches = 180 # 180 branches
    third_tree_height = 60 # 60 feet tall
    third_tree_bpf = third_tree_branches / third_tree_height

    # L4
    fourth_tree_branches = 153 # 153 branches
    fourth_tree_height = 34 # 34 feet tall
    fourth_tree_bpf = fourth_tree_branches / fourth_tree_height

    # L5
    total_bpf = first_tree_bpf + second_tree_bpf + third_tree_bpf + fourth_tree_bpf

    # L6
    num_trees = 4 # WK
    average_bpf = total_bpf / num_trees

    # FA
    answer = average_bpf
    return answer