def solve():
    """Index: 2487.
    Returns: the total cost the baker will have to pay for all ingredients.
    """
    # L1
    num_boxes_flour = 3 # 3 boxes of flour
    cost_per_box_flour = 3 # $3 each box
    total_cost_flour = num_boxes_flour * cost_per_box_flour

    # L2
    num_trays_eggs = 3 # 3 trays of eggs
    cost_per_tray_eggs = 10 # $10 for each tray
    total_cost_eggs = num_trays_eggs * cost_per_tray_eggs

    # L3
    num_liters_milk = 7 # 7 liters of milk
    cost_per_liter_milk = 5 # $5 each liter
    total_cost_milk = num_liters_milk * cost_per_liter_milk

    # L4
    num_boxes_baking_soda = 2 # 2 boxes of baking soda
    cost_per_box_baking_soda = 3 # $3 each box
    total_cost_baking_soda = num_boxes_baking_soda * cost_per_box_baking_soda

    # L5
    total_cost_all_ingredients = total_cost_flour + total_cost_eggs + total_cost_milk + total_cost_baking_soda

    # FA
    answer = total_cost_all_ingredients
    return answer