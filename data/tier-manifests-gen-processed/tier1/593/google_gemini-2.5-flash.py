def solve():
    """Index: 593.
    Returns: the depth of the drift at the end of the first day.
    """
    # L1
    snow_day3 = 6 # adding another 6 inches of snow
    snow_day4 = 18 # another 18 inches of snow fell
    total_snow_day3_4 = snow_day3 + snow_day4

    # L2
    final_depth_day4 = 34 # was 34 inches deep at the end of the fourth day
    depth_after_melt_before_snow = final_depth_day4 - total_snow_day3_4

    # L3
    multiplier_for_original_depth = 2 # half of the snowdrift melted
    original_depth_day1 = multiplier_for_original_depth * depth_after_melt_before_snow

    # FA
    answer = original_depth_day1
    return answer