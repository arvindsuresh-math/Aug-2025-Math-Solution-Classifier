def solve():
    """Index: 7066.
    Returns: the total amount the school spent.
    """
    # L1
    cartons_of_pencils = 20 # 20 cartons of pencils
    boxes_per_carton_pencils = 10 # cartons of 10 boxes
    total_boxes_pencils = cartons_of_pencils * boxes_per_carton_pencils

    # L2
    cost_per_box_pencils = 2 # each box costs $2
    total_cost_pencils = total_boxes_pencils * cost_per_box_pencils

    # L3
    cartons_of_markers = 10 # 10 cartons of markers
    boxes_per_carton_markers = 5 # A carton has 5 boxes
    total_boxes_markers = cartons_of_markers * boxes_per_carton_markers

    # L4
    cost_per_box_markers = 4 # costs $4 (interpreted as per box based on solution calculation)
    total_cost_markers = total_boxes_markers * cost_per_box_markers

    # L5
    total_spent = total_cost_pencils + total_cost_markers

    # FA
    answer = total_spent
    return answer