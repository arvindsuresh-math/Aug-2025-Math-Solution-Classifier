def solve():
    """Index: 7033.
    Returns: the number of hours each middle guard will take.
    """
    # L1
    first_guard_hours = 3 # The first guard would take three hours
    last_guard_hours = 2 # the last guard would wake up early and take two hours
    hours_taken_by_first_and_last_guard = first_guard_hours + last_guard_hours

    # L2
    total_shift_hours = 9 # cover the nine hours of the night shift
    remaining_hours_for_middle_guards = total_shift_hours - hours_taken_by_first_and_last_guard

    # L3
    num_middle_guards = 2 # the middle two guards
    hours_per_middle_guard = remaining_hours_for_middle_guards / num_middle_guards

    # FA
    answer = hours_per_middle_guard
    return answer