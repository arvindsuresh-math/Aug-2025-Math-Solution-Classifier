def solve():
    """Index: 6754.
    Returns: the number of pictures Randy drew.
    """
    # L1
    quincy_more_than_peter = 20 # Quincy drew 20 more pictures than Peter
    peter_pictures = 8 # Peter drew 8 pictures
    quincy_pictures = quincy_more_than_peter + peter_pictures

    # L2
    quincy_peter_total = quincy_pictures + peter_pictures

    # L3
    total_pictures = 41 # drew 41 pictures altogether
    randy_pictures = total_pictures - quincy_peter_total

    # FA
    answer = randy_pictures
    return answer