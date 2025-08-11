def solve():
    """Index: 2170.
    Returns: the total amount the two girls spend altogether.
    """
    # L1
    barrette_cost_per_set = 3 # One set of barrettes costs $3 each
    comb_cost_per_unit = 1 # one comb costs $1 each
    kristine_total_spend = barrette_cost_per_set + comb_cost_per_unit

    # L2
    crystal_barrettes_sets = 3 # three sets of barrettes
    crystal_barrettes_cost = crystal_barrettes_sets * barrette_cost_per_set

    # L3
    crystal_total_spend = crystal_barrettes_cost + comb_cost_per_unit

    # L4
    total_spend_altogether = kristine_total_spend + crystal_total_spend

    # FA
    answer = total_spend_altogether
    return answer