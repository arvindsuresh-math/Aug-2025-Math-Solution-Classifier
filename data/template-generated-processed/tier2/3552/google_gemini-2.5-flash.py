def solve():
    """Index: 3552.
    Returns: the total number of ridges on all of Jerry's records.
    """
    # L1
    num_cases = 4 # 4 cases
    shelves_per_case = 3 # 3 shelves
    records_per_shelf = 20 # 20 records each
    total_capacity_records = num_cases * shelves_per_case * records_per_shelf

    # L2
    full_percent_num = 60 # 60% full
    percent_factor = 0.01 # WK
    actual_records = total_capacity_records * full_percent_num * percent_factor

    # L3
    ridges_per_record = 60 # 60 ridges on a vinyl record
    total_ridges = actual_records * ridges_per_record

    # FA
    answer = total_ridges
    return answer