def solve():
    """Index: 3265.
    Returns: the length of Carmen's brush in centimeters.
    """
    # L1
    carla_brush_length_inches = 12 # Carla's brush is 12 inches long
    carmen_longer_percent_num = 150 # 50% longer than Carla's brush (100% + 50%)
    percent_factor = 0.01 # WK
    carmen_brush_length_inches = carmen_longer_percent_num * percent_factor * carla_brush_length_inches

    # L2
    cm_per_inch = 2.5 # 2.5 centimeters per inch
    carmen_brush_length_cm = carmen_brush_length_inches * cm_per_inch

    # FA
    answer = carmen_brush_length_cm
    return answer