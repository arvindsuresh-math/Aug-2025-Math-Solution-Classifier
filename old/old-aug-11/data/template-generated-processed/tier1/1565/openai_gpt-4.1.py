def solve():
    """Index: 1565.
    Returns: the total number of minutes Jane spends waiting for her nail polish to dry.
    """
    # L1
    color_coat_dry_time = 3 # 3 minutes each to dry
    num_color_coats = 2 # two color coats
    total_color_coat_time = color_coat_dry_time * num_color_coats

    # L2
    base_coat_dry_time = 2 # base coat that takes 2 minutes to dry
    top_coat_dry_time = 5 # top coat that takes 5 minutes to dry
    total_time = total_color_coat_time + base_coat_dry_time + top_coat_dry_time

    # FA
    answer = total_time
    return answer