def solve():
    """Index: 5882.
    Returns: the number of loaves of bread needed.
    """
    # L1
    suzanne_slice_count = 1 # She and her husband each have 1 whole slice
    husband_slice_count = 1 # She and her husband each have 1 whole slice
    daughter_individual_share = 0.5 # her daughters split 1 slice (calculation uses .5+.5)
    slices_per_day = suzanne_slice_count + husband_slice_count + daughter_individual_share + daughter_individual_share

    # L2
    days_per_weekend = 2 # On Saturdays and Sundays
    slices_per_weekend = slices_per_day * days_per_weekend

    # L3
    num_weeks = 52 # Over 52 weeks
    total_slices_needed = slices_per_weekend * num_weeks

    # L4
    slices_per_loaf = 12 # 12 slices per loaf
    total_loaves_needed = total_slices_needed / slices_per_loaf

    # FA
    answer = total_loaves_needed
    return answer