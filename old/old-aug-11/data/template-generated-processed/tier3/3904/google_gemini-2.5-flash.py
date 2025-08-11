def solve():
    """Index: 3904.
    Returns: the cost of the set of paints.
    """
    # L1
    num_classes = 6 # 6 classes
    folders_per_class = 1 # 1 folder for each class
    total_folders = num_classes * folders_per_class

    # L2
    pencils_per_class = 3 # 3 pencils for each class
    total_pencils = num_classes * pencils_per_class

    # L3
    pencils_per_eraser = 6 # for every 6 pencils she should have 1 eraser
    total_erasers = total_pencils / pencils_per_eraser

    # L4
    cost_per_folder = 6 # Folders cost $6
    cost_folders = total_folders * cost_per_folder

    # L5
    cost_per_pencil = 2 # pencils cost $2
    cost_pencils = total_pencils * cost_per_pencil

    # L6
    cost_per_eraser = 1 # erasers cost $1
    cost_erasers = total_erasers * cost_per_eraser

    # L7
    total_cost_supplies = cost_folders + cost_pencils + cost_erasers

    # L8
    total_spent = 80 # If she spends $80
    cost_paint_set = total_spent - total_cost_supplies

    # FA
    answer = cost_paint_set
    return answer