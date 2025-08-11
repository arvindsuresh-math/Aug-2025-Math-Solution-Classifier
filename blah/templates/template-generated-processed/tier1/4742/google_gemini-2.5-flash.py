def solve():
    """Index: 4742.
    Returns: the total cost to send all gifts by mail to relatives.
    """
    # L1
    num_parents = 2 # two parents
    num_brothers = 3 # three brothers
    parents_and_siblings = num_parents + num_brothers

    # L2
    children_per_brother = 2 # 2 children each
    spouse_per_brother = 1 # WK
    people_per_brother_family = spouse_per_brother + children_per_brother

    # L3
    relatives_from_brothers_families = num_brothers * people_per_brother_family

    # L4
    total_relatives = parents_and_siblings + relatives_from_brothers_families

    # L5
    cost_per_package = 5 # $5 per package
    total_cost = total_relatives * cost_per_package

    # FA
    answer = total_cost
    return answer