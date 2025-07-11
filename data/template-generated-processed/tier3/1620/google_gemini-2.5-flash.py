def solve():
    """Index: 1620.
    Returns: the number of additional drying racks Michelle needs.
    """
    # L1
    num_bags_flour = 3 # three 8-cup bags of flour
    cups_per_bag = 8 # 8-cup bags of flour
    total_cups_flour = num_bags_flour * cups_per_bag

    # L2
    cups_per_pound_dough = 2 # two cups of flour to make each pound of pasta dough
    total_pounds_dough = total_cups_flour / cups_per_pound_dough

    # L3
    pounds_per_rack = 3 # a drying rack for each three pounds of pasta
    racks_needed = total_pounds_dough / pounds_per_rack

    # L4
    racks_owned = 3 # She owns three racks right now
    additional_racks_needed = racks_needed - racks_owned

    # FA
    answer = additional_racks_needed
    return answer