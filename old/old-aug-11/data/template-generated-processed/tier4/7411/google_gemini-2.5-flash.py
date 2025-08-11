def solve():
    """Index: 7411.
    Returns: the original height of the tree in feet.
    """
    # L1
    current_height_inches = 180 # 180 inches tall
    percentage_increase = 50 # 50% taller
    initial_percentage = 100 # WK
    total_percentage = initial_percentage + percentage_increase

    # L2
    inches_per_percent = current_height_inches / total_percentage

    # L3
    original_height_inches = inches_per_percent * initial_percentage

    # L4
    inches_per_foot = 12 # WK
    original_height_feet = original_height_inches / inches_per_foot

    # FA
    answer = original_height_feet
    return answer