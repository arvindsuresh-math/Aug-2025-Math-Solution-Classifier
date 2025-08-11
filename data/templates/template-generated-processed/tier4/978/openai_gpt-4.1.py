def solve():
    """Index: 978.
    Returns: the number of female worker ants in Stephen's ant farm.
    """
    # L1
    total_ants = 110 # Stephen has 110 ants in his ant farm
    worker_fraction = 2 # Half of the ants are worker ants
    worker_ants = total_ants / worker_fraction

    # L2
    male_worker_percent = 0.20 # 20 percent of the worker ants are male
    male_worker_ants = worker_ants * male_worker_percent

    # L3
    female_worker_ants = worker_ants - male_worker_ants

    # FA
    answer = female_worker_ants
    return answer