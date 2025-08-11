def solve():
    """Index: 7295.
    Returns: the total square miles of both plains.
    """
    # L1
    plain_b_area = 200 # If plain B has 200 square miles
    less_than_plain_b = 50 # 50 square miles less than the region east of plain B
    plain_a_area = plain_b_area - less_than_plain_b

    # L2
    total_area = plain_a_area + plain_b_area

    # FA
    answer = total_area
    return answer