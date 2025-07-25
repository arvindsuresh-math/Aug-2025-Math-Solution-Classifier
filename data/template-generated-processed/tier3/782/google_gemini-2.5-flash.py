def solve():
    """Index: 782.
    Returns: the total number of hours Melissa has to work.
    """
    # L1
    total_fabric = 56 # 56 square meters of fabric
    fabric_per_dress = 4 # each dress takes 4 square meters of fabric
    num_dresses = total_fabric / fabric_per_dress

    # L2
    hours_per_dress = 3 # 3 hours to make
    total_work_hours = num_dresses * hours_per_dress

    # FA
    answer = total_work_hours
    return answer