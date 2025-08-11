def solve():
    """Index: 5912.
    Returns: the total amount Selene and Tanya spend together.
    """
    # L1
    num_sandwiches_selene = 3 # three sandwiches
    cost_sandwich = 2 # a sandwich at $2
    cost_selene_sandwiches = num_sandwiches_selene * cost_sandwich

    # L2
    cost_fruit_juice = 2 # a can of fruit juice at $2 each can
    total_selene_spend = cost_selene_sandwiches + cost_fruit_juice

    # L3
    num_hamburgers_tanya = 2 # two hamburgers
    cost_hamburger = 2 # a hamburger at $2
    cost_tanya_hamburgers = num_hamburgers_tanya * cost_hamburger

    # L4
    num_fruit_juice_tanya = 2 # two cans of fruit juice
    cost_tanya_fruit_juice = num_fruit_juice_tanya * cost_fruit_juice

    # L5
    total_tanya_spend = cost_tanya_hamburgers + cost_tanya_fruit_juice

    # L6
    total_combined_spend = total_selene_spend + total_tanya_spend

    # FA
    answer = total_combined_spend
    return answer