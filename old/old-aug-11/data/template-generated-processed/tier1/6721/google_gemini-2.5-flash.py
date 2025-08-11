def solve():
    """Index: 6721.
    Returns: the height of the tree in inches after 8 years.
    """
    # L1
    growth_per_year = 5 # Each year it grows 5 feet
    num_years = 8 # In 8 years
    total_growth_feet = growth_per_year * num_years

    # L2
    initial_height_feet = 52 # The height of the tree in Kilmer Park is 52 feet
    final_height_feet = initial_height_feet + total_growth_feet

    # L3
    inches_per_foot = 12 # 1 foot is 12 inches
    final_height_inches = final_height_feet * inches_per_foot

    # FA
    answer = final_height_inches
    return answer