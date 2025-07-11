def solve():
    """Index: 2358.
    Returns: the total cost to buy the office supplies.
    """
    # L1
    num_dozens_pencils = 2 # two dozen pencils
    items_per_dozen = 12 # WK
    total_pencils = num_dozens_pencils * items_per_dozen

    # L2
    cost_per_pencil = 0.5 # A pencil costs $0.5 each
    total_cost_pencils = cost_per_pencil * total_pencils

    # L3
    cost_per_folder = 0.9 # a folder costs $0.9 each
    num_folders = 20 # 20 pieces of folders
    total_cost_folders = cost_per_folder * num_folders

    # L4
    total_office_supplies_cost = total_cost_pencils + total_cost_folders

    # FA
    answer = total_office_supplies_cost
    return answer