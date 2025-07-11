def solve():
    """Index: 600.
    Returns: the number of minutes it will take Mike to finish typing the document.
    """
    # L1
    original_speed = 65 # Mike can type 65 words per minute
    speed_loss = 20 # his typing speed is now 20 words less per minute
    reduced_speed = original_speed - speed_loss

    # L2
    document_length = 810 # supposed to type a document with 810 words
    minutes_needed = document_length / reduced_speed

    # FA
    answer = minutes_needed
    return answer