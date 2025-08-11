def solve():
    """Index: 5786.
    Returns: the number of bags of popcorn Shelby has left for the party.
    """
    # L1
    dozen_bags_buttered_popcorn = 12 # a dozen bags of buttered popcorn
    caramel_popcorn_initial = 10 # 10 bags of caramel popcorn
    total_initial_popcorn = dozen_bags_buttered_popcorn + caramel_popcorn_initial

    # L2
    alan_took_buttered = 3 # 3 bags of buttered popcorn
    alan_took_caramel = 1 # 1 bag of caramel popcorn
    alan_took_total = alan_took_buttered + alan_took_caramel

    # L3
    popcorn_left = total_initial_popcorn - alan_took_total

    # FA
    answer = popcorn_left
    return answer