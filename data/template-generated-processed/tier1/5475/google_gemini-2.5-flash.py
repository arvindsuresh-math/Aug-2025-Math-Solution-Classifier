def solve():
    """Index: 5475.
    Returns: Devin's chances of making the basketball team.
    """
    # L1
    initial_height = 65 # 65 inches tall
    height_growth = 3 # grows 3 inches
    new_height = initial_height + height_growth

    # L2
    base_height_for_chance = 66 # 66 inches
    extra_inches = new_height - base_height_for_chance

    # L3
    percentage_increase_per_inch = 10 # increase 10% for every additional inch
    total_percentage_increase = extra_inches * percentage_increase_per_inch

    # L4
    base_chance_percentage = 10 # start at 10%
    overall_chance = base_chance_percentage + total_percentage_increase

    # FA
    answer = overall_chance
    return answer