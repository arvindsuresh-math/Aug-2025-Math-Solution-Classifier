def solve():
    """Index: 371.
    Returns: the number of additional sessions needed to cook all hamburgers.
    """
    # L1
    total_hamburgers_needed = 115 # 115 hamburgers in total
    hamburgers_already_cooked = 40 # already cooked 40 hamburgers
    hamburgers_remaining_to_cook = total_hamburgers_needed - hamburgers_already_cooked

    # L2
    hamburgers_per_session = 15 # 15 hamburgers per session
    sessions_needed = hamburgers_remaining_to_cook / hamburgers_per_session

    # FA
    answer = sessions_needed
    return answer