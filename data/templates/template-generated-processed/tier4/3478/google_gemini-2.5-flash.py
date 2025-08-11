def solve():
    """Index: 3478.
    Returns: the total cost to buy all the supplies for S'mores.
    """
    # L1
    num_friends = 8 # 8 of them in total
    smores_per_person = 3 # each eat 3 S'mores
    total_smores = num_friends * smores_per_person

    # L2
    cost_per_batch = 3 # It costs $3 in supplies
    smores_per_batch = 4 # to make 4 S'mores
    cost_per_smore = cost_per_batch / smores_per_batch

    # L3
    total_cost = total_smores * cost_per_smore

    # FA
    answer = total_cost
    return answer