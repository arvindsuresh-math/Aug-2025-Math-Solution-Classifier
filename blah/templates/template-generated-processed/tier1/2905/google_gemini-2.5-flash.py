def solve():
    """Index: 2905.
    Returns: the total length of the rubber, the pen, and the pencil altogether.
    """
    # L1
    pencil_length = 12 # pencil is 12 centimeters long
    pen_shorter_than_pencil = 2 # shorter than the pencil by 2 centimeters
    pen_length = pencil_length - pen_shorter_than_pencil

    # L2
    pen_longer_than_rubber = 3 # longer than the rubber by 3 centimeters
    rubber_length = pen_length - pen_longer_than_rubber

    # L3
    total_length = rubber_length + pen_length + pencil_length

    # FA
    answer = total_length
    return answer