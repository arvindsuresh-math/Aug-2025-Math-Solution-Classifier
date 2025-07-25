def solve():
    """Index: 6333.
    Returns: the number of additional plants Justice needs.
    """
    # L1
    ferns = 3 # 3 ferns
    palms = 5 # 5 palms
    succulents = 7 # 7 succulent plants
    current_plants = ferns + palms + succulents

    # L2
    total_desired_plants = 24 # total of 24 plants
    plants_needed = total_desired_plants - current_plants

    # FA
    answer = plants_needed
    return answer