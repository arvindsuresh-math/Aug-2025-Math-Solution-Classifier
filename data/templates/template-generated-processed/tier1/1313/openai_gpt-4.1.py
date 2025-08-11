def solve():
    """Index: 1313.
    Returns: the maximum additional minutes Frank can spend in the current maze to keep his average at or below 60 minutes per maze.
    """
    # L1
    total_mazes = 5 # 4 other mazes + current maze
    max_avg = 60 # average doesn't go above 60 minutes per maze
    max_total_time = total_mazes * max_avg

    # L2
    other_mazes = 4 # 4 other corn mazes
    avg_other = 50 # finished those in 50 minutes on average
    total_other_time = other_mazes * avg_other

    # L3
    current_time = 45 # already spent 45 minutes inside
    time_so_far = total_other_time + current_time

    # L4
    max_additional_time = max_total_time - time_so_far

    # FA
    answer = max_additional_time
    return answer