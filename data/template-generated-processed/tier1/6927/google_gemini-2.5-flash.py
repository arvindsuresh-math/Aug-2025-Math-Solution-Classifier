def solve():
    """Index: 6927.
    Returns: the total money Mrs. Martin pays the cashier for all ice creams.
    """
    # L1
    cost_regular_scoop = 4 # A regular scoop is $4
    num_regular_scoops = 2 # Mr. and Mrs. Martin each get the regular scoop
    cost_total_regular = cost_regular_scoop * num_regular_scoops

    # L2
    cost_kiddie_scoop = 3 # A kiddie scoop is $3
    num_kiddie_scoops = 2 # Their two children each get the kiddie scoop
    cost_total_kiddie = cost_kiddie_scoop * num_kiddie_scoops

    # L3
    cost_double_scoop = 6 # A double scoop is $6
    num_double_scoops = 3 # Their three teenage children each get double scoops
    cost_total_double = cost_double_scoop * num_double_scoops

    # L4
    total_cost = cost_total_regular + cost_total_kiddie + cost_total_double

    # FA
    answer = total_cost
    return answer