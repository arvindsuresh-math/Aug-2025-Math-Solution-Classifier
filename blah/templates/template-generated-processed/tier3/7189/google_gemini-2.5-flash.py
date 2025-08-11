def solve():
    """Index: 7189.
    Returns: the percentage of girls in the class.
    """
    # L1
    initial_boys = 11 # 11 boys
    added_boy = 1 # 1 boy is added
    total_boys = initial_boys + added_boy

    # L2
    girls = 13 # 13 girls
    total_students = total_boys + girls

    # L3
    percentage_multiplier = 100 # WK
    percentage_girls = (girls / total_students) * percentage_multiplier

    # FA
    answer = percentage_girls
    return answer