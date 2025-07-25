def solve():
    """Index: 5800.
    Returns: the number of additional drawings Anne can make.
    """
    # L1
    num_markers = 12 # 12 markers
    drawings_per_marker = 1.5 # each one lasts for about 1.5 drawings
    total_drawings_capacity = num_markers * drawings_per_marker

    # L2
    drawings_already_made = 8 # she has already made 8 drawings
    remaining_drawings = total_drawings_capacity - drawings_already_made

    # FA
    answer = remaining_drawings
    return answer