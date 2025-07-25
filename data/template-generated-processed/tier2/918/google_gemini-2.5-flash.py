def solve():
    """Index: 918.
    Returns: the total square feet of shingles needed to roof the house and the porch.
    """
    # L1
    house_length = 20.5 # 20.5 feet
    house_width = 10 # 10 feet
    house_area = house_length * house_width

    # L2
    porch_length = 6 # 6 feet
    porch_width = 4.5 # 4.5 feet
    porch_area = porch_length * porch_width

    # L3
    total_shingles_needed = house_area + porch_area

    # FA
    answer = total_shingles_needed
    return answer