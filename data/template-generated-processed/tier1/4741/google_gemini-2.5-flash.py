def solve():
    """Index: 4741.
    Returns: the total number of clouds counted.
    """
    # L1
    carson_clouds = 6 # Carson counts 6 clouds
    multiplier_brother = 3 # three times as many clouds
    brother_clouds = carson_clouds * multiplier_brother

    # L2
    total_clouds = brother_clouds + carson_clouds

    # FA
    answer = total_clouds
    return answer