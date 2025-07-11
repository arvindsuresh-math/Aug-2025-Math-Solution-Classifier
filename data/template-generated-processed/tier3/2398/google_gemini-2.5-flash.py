def solve():
    """Index: 2398.
    Returns: the length of each part in inches.
    """
    # L1
    feet_length = 5 # 5 feet 4 inches long
    inches_per_foot = 12 # 1 foot is equal to 12 inches
    feet_in_inches = feet_length * inches_per_foot

    # L2
    remaining_inches = 4 # 5 feet 4 inches long
    total_length_inches = feet_in_inches + remaining_inches

    # L3
    num_parts = 4 # divided into 4 equal parts
    length_each_part = total_length_inches / num_parts

    # FA
    answer = length_each_part
    return answer