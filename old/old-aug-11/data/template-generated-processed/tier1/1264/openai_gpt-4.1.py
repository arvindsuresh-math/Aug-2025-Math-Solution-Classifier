def solve():
    """Index: 1264.
    Returns: the total number of pixels on the monitor.
    """
    # L1
    width_inches = 21 # 21 inches
    dots_per_inch = 100 # 100 dots per inch
    width_pixels = width_inches * dots_per_inch

    # L2
    height_inches = 12 # 12 inches
    height_pixels = height_inches * dots_per_inch

    # L3
    total_pixels = width_pixels * height_pixels

    # FA
    answer = total_pixels
    return answer