def solve():
    """Index: 2358.
    Returns: the total cost to buy the office supplies.
    """
    # L1
    num_dozen = 2 # two dozen pencils
    pencils_per_dozen = 12 # WK
    total_pencils = num_dozen * pencils_per_dozen

    # L2
    pencil_cost = 0.5 # pencil costs $0.5 each
    total_pencil_cost = pencil_cost * total_pencils

    # L3
    folder_cost = 0.9 # folder costs $0.9 each
    num_folders = 20 # 20 pieces of folders
    total_folder_cost = folder_cost * num_folders

    # L4
    total_cost = total_pencil_cost + total_folder_cost

    # FA
    answer = total_cost
    return answer