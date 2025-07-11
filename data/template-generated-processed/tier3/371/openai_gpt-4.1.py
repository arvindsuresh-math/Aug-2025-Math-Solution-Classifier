def solve():
    """Index: 371.
    Returns: the number of additional grilling sessions Ronald needs to finish cooking all hamburgers.
    """
    # L1
    total_hamburgers = 115 # cook 115 hamburgers in total
    already_cooked = 40 # has already cooked 40 hamburgers
    hamburgers_left = total_hamburgers - already_cooked

    # L2
    hamburgers_per_session = 15 # can grill 15 hamburgers per session
    sessions_needed = hamburgers_left / hamburgers_per_session

    # FA
    answer = sessions_needed
    return answer