def solve():
    """Index: 539.
    Returns: the number of trees the company needs to plant.
    """
    # L1
    trees_chopped_first_half = 200 # chopped down 200 trees in the first half of the year
    trees_chopped_second_half = 300 # 300 more trees in the second half of the year
    total_trees_chopped = trees_chopped_first_half + trees_chopped_second_half

    # L2
    trees_planted_per_chopped = 3 # plant three more for every tree they chop
    total_trees_to_plant = total_trees_chopped * trees_planted_per_chopped

    # FA
    answer = total_trees_to_plant
    return answer