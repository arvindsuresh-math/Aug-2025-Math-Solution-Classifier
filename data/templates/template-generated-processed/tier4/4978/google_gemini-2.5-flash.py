def solve():
    """Index: 4978.
    Returns: the number of seeds Bob can plant in each row.
    """
    # L1
    seed_space_inches = 18 # 18 inches to its right
    inches_per_foot = 12 # WK
    seed_space_feet = seed_space_inches / inches_per_foot

    # L2
    row_length_feet = 120 # The rows are 120 feet long
    num_seeds_per_row = row_length_feet / seed_space_feet

    # FA
    answer = num_seeds_per_row
    return answer