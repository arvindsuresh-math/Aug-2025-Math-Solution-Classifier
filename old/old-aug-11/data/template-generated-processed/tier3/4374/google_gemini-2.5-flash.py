def solve():
    """Index: 4374.
    Returns: the number of jars of peanut butter Phoebe needs.
    """
    # L1
    phoebe_servings_per_day = 1 # 1 serving
    dog_servings_per_day = 1 # 1 serving
    total_servings_per_day = phoebe_servings_per_day + dog_servings_per_day

    # L2
    number_of_days = 30 # 30 days
    total_servings_needed = number_of_days * total_servings_per_day

    # L3
    servings_per_jar = 15 # 15 servings
    jars_needed = total_servings_needed / servings_per_jar

    # FA
    answer = jars_needed
    return answer