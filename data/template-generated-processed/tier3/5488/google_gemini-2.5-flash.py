def solve():
    """Index: 5488.
    Returns: the total number of cell phones in Delaware.
    """
    # L1
    population_delaware = 974000 # The population of Delaware is 974,000
    people_per_group = 1000 # per 1000 people
    num_groups = population_delaware / people_per_group

    # L2
    cell_phones_per_group = 673 # 673 cell phones per 1000 people
    total_cell_phones = num_groups * cell_phones_per_group

    # FA
    answer = total_cell_phones
    return answer