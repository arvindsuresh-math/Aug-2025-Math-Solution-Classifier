def solve():
    """Index: 3120.
    Returns: the total number of soaps in 2 boxes.
    """
    # L1
    soaps_per_package = 192 # 192 soaps in a package
    packages_per_box = 6 # each box contains 6 packages
    soaps_in_one_box = soaps_per_package * packages_per_box

    # L2
    num_boxes = 2 # 2 big boxes
    total_soaps = soaps_in_one_box * num_boxes

    # FA
    answer = total_soaps
    return answer