def solve():
    """Index: 6436.
    Returns: the number of more points Layla scored than Nahima.
    """
    # L1
    total_points = 112 # The total number of points scored was 112
    layla_points = 70 # Layla won with 70 points
    nahima_points = total_points - layla_points

    # L2
    layla_more_than_nahima = layla_points - nahima_points

    # FA
    answer = layla_more_than_nahima
    return answer