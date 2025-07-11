def solve():
    """Index: 186.
    Returns: the total length of all snakes combined in inches.
    """
    # L1
    first_snake_feet = 2 # 1 snake is 2 feet long
    inches_per_foot = 12 # WK
    first_snake_inches = first_snake_feet * inches_per_foot

    # L2
    second_snake_inches = 16 # Another snake is 16 inches long
    third_snake_inches = 10 # The last snake is 10 inches long
    total_inches = first_snake_inches + second_snake_inches + third_snake_inches

    # FA
    answer = total_inches
    return answer