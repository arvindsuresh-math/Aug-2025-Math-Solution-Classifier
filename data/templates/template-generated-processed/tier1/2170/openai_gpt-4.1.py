def solve():
    """Index: 2170.
    Returns: the total amount the two girls spend altogether.
    """
    # L1
    barrette_cost = 3 # barrettes costs $3 each
    comb_cost = 1 # comb costs $1 each
    kristine_barrettes = 1 # Kristine buys one set of barrettes
    kristine_combs = 1 # Kristine buys one comb
    kristine_spent = barrette_cost * kristine_barrettes + comb_cost * kristine_combs

    # L2
    crystal_barrettes = 3 # Crystal buys three sets of barrettes
    crystal_barrettes_cost = crystal_barrettes * barrette_cost

    # L3
    crystal_combs = 1 # Crystal buys one comb
    crystal_spent = crystal_barrettes_cost + comb_cost * crystal_combs

    # L4
    total_spent = kristine_spent + crystal_spent

    # FA
    answer = total_spent
    return answer