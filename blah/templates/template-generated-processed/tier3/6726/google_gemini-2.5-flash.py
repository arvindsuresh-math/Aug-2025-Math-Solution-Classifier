def solve():
    """Index: 6726.
    Returns: the number of months it will take for the poem to contain 90 lines.
    """
    # L1
    target_lines = 90 # poem contain 90 lines
    current_lines = 24 # currently contains 24 lines
    lines_to_add = target_lines - current_lines

    # L2
    lines_per_month = 3 # adds 3 lines to the poem every month
    months_needed = lines_to_add / lines_per_month

    # FA
    answer = months_needed
    return answer