def solve():
    """Index: 5058.
    Returns: the total number of trees planted by all grades.
    """
    # L1
    fourth_graders_trees = 30 # 4th graders planted a total of 30 trees
    multiplier_for_fifth_graders = 2 # 5th graders planted twice as many
    fifth_graders_trees = fourth_graders_trees * multiplier_for_fifth_graders

    # L2
    multiplier_for_thrice = 3 # thrice the number of trees
    thrice_fifth_graders_trees = fifth_graders_trees * multiplier_for_thrice

    # L3
    fewer_than_thrice = 30 # 30 fewer than thrice
    sixth_graders_trees = thrice_fifth_graders_trees - fewer_than_thrice

    # L4
    total_trees = fourth_graders_trees + fifth_graders_trees + sixth_graders_trees

    # FA
    answer = total_trees
    return answer