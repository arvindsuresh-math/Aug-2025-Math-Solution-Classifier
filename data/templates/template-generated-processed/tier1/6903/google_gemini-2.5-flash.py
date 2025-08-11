def solve():
    """Index: 6903.
    Returns: the total number of beads Hearty has.
    """
    # L1
    num_blue_packages = 3 # 3 packages of blue
    num_red_packages = 5 # 5 packages of red
    total_packages = num_blue_packages + num_red_packages

    # L2
    beads_per_package = 40 # 40 beads in each package
    total_beads = total_packages * beads_per_package

    # FA
    answer = total_beads
    return answer