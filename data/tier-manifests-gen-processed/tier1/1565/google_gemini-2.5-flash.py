def solve():
    """Index: 1565.
    Returns: the total minutes Jane spends waiting for her nail polish to dry.
    """
    # L1
    drying_time_per_color_coat = 3 # 3 minutes each to dry
    num_color_coats = 2 # two color coats
    total_color_coat_drying_time = drying_time_per_color_coat * num_color_coats

    # L2
    base_coat_drying_time = 2 # 2 minutes to dry
    top_coat_drying_time = 5 # 5 minutes to dry
    total_drying_time = total_color_coat_drying_time + base_coat_drying_time + top_coat_drying_time

    # FA
    answer = total_drying_time
    return answer