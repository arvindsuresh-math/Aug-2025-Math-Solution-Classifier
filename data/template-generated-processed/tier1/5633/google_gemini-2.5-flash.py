def solve():
    """Index: 5633.
    Returns: the number of charcoal drawings.
    """
    # L1
    colored_pencil_drawings = 14 # 14 of the drawings were made using colored pencils
    blending_marker_drawings = 7 # 7 of the drawings were made using blending markers
    non_charcoal_drawings = colored_pencil_drawings + blending_marker_drawings

    # L2
    total_drawings = 25 # 25 drawings to display
    charcoal_drawings = total_drawings - non_charcoal_drawings

    # FA
    answer = charcoal_drawings
    return answer