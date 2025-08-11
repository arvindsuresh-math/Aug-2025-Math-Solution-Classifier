def solve():
    """Index: 1264.
    Returns: the total number of pixels.
    """
    # L1
    monitor_width_inches = 21 # 21 inches
    dots_per_inch = 100 # 100 dots per inch
    pixels_across = monitor_width_inches * dots_per_inch

    # L2
    monitor_height_inches = 12 # 12 inches
    pixels_tall = monitor_height_inches * dots_per_inch

    # L3
    total_pixels = pixels_across * pixels_tall

    # FA
    answer = total_pixels
    return answer