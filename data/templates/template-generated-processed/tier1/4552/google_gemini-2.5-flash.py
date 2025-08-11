def solve():
    """Index: 4552.
    Returns: the total number of subjects taken by Millie, Monica, and Marius.
    """
    # L1
    monica_subjects = 10 # Monica took 10 subjects
    marius_more_than_monica = 4 # 4 subjects more than Monica
    marius_subjects = monica_subjects + marius_more_than_monica

    # L2
    marius_monica_total = marius_subjects + monica_subjects

    # L3
    millie_more_than_marius = 3 # three more subjects than Marius
    millie_subjects = marius_subjects + millie_more_than_marius

    # L4
    total_subjects = marius_monica_total + millie_subjects

    # FA
    answer = total_subjects
    return answer