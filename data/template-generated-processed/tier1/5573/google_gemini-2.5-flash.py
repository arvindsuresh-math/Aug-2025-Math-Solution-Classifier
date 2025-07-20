def solve():
    """Index: 5573.
    Returns: the total number of muffins Amy originally baked.
    """
    # L1
    muffins_monday = 1 # 1 muffin to school
    increase_per_day = 1 # one more muffin to school than she did the day before
    muffins_tuesday = muffins_monday + increase_per_day

    # L2
    muffins_wednesday = muffins_tuesday + increase_per_day

    # L3
    muffins_thursday = muffins_wednesday + increase_per_day

    # L4
    muffins_friday = muffins_thursday + increase_per_day

    # L5
    total_muffins_brought = muffins_monday + muffins_tuesday + muffins_wednesday + muffins_thursday + muffins_friday

    # L6
    muffins_left_saturday = 7 # 7 muffins left
    total_baked = total_muffins_brought + muffins_left_saturday

    # FA
    answer = total_baked
    return answer