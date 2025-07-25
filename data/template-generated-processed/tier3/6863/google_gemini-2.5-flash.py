def solve():
    """Index: 6863.
    Returns: the total number of trees chopped down.
    """
    # L1
    total_firewood_pieces = 500 # chopped 500 pieces of firewood
    pieces_per_log = 5 # each log is then chopped into 5 pieces of firewood
    total_logs = total_firewood_pieces / pieces_per_log

    # L2
    logs_per_tree = 4 # produces 4 logs each
    total_trees = total_logs / logs_per_tree

    # FA
    answer = total_trees
    return answer