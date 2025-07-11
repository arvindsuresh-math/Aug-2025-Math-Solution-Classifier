def solve():
    """Index: 600.
    Returns: the time it will take Mike to finish typing the document.
    """
    # L1
    initial_typing_speed = 65 # 65 words per minute
    speed_reduction = 20 # 20 words less per minute
    new_typing_speed = initial_typing_speed - speed_reduction

    # L2
    document_length = 810 # document with 810 words
    time_to_finish = document_length / new_typing_speed

    # FA
    answer = time_to_finish
    return answer