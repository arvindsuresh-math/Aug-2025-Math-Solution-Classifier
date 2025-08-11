def solve():
    """Index: 5316.
    Returns: the number of slices of bread Shane will have leftover.
    """
    # L1
    num_ham_packages = 2 # 2 packages of sliced ham
    slices_per_ham_package = 8 # 8 slices each
    total_ham_slices = num_ham_packages * slices_per_ham_package

    # L2
    num_sandwiches_made = total_ham_slices # makes as many sandwiches as he can according to the ham he has

    # L3
    slices_per_bread_package = 20 # 20 slices each
    num_bread_packages = 2 # 2 packages of sliced bread
    total_bread_slices = slices_per_bread_package * num_bread_packages

    # L4
    slices_per_sandwich = 2 # WK
    bread_needed = num_sandwiches_made * slices_per_sandwich

    # L5
    bread_leftover = total_bread_slices - bread_needed

    # FA
    answer = bread_leftover
    return answer