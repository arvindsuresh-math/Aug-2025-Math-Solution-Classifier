def solve():
    """Index: 7441.
    Returns: the total number of pictures drawn by Randy, Peter, and Quincy.
    """
    # L1
    randy_pictures = 5 # Randy drew 5 pictures
    peter_more_than_randy = 3 # 3 more pictures than Randy
    peter_pictures = randy_pictures + peter_more_than_randy

    # L2
    quincy_more_than_peter = 20 # 20 more pictures than Peter
    quincy_pictures = quincy_more_than_peter + peter_pictures

    # L3
    total_pictures = randy_pictures + peter_pictures + quincy_pictures

    # FA
    answer = total_pictures
    return answer