def solve():
    """Index: 5385.
    Returns: the total number of people at the dance.
    """
    # L1
    girls_at_dance = 60 # 60 girls at the dance
    girls_ratio_parts = 4 # The ratio of boys to girls at the dance was 3:4
    one_part_students = girls_at_dance / girls_ratio_parts

    # L2
    boys_ratio_parts = 3 # The ratio of boys to girls at the dance was 3:4
    boys_at_dance = one_part_students * boys_ratio_parts

    # L3
    teachers_percentage = 0.2 # teachers were 20% of the number of boys
    teachers_at_dance = boys_at_dance * teachers_percentage

    # L4
    total_people_at_dance = girls_at_dance + boys_at_dance + teachers_at_dance

    # FA
    answer = total_people_at_dance
    return answer