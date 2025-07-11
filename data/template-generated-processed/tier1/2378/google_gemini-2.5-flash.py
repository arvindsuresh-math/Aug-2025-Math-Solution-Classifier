def solve():
    """Index: 2378.
    Returns: the total amount Tony paid for all items.
    """
    # L1
    num_lego_sets = 3 # 3 sets of lego
    cost_per_lego_set = 250 # $250 a set of Lego blocks
    total_cost_legos = num_lego_sets * cost_per_lego_set

    # L2
    num_toy_swords = 7 # 7 toy swords
    cost_per_toy_sword = 120 # $120 worth toy sword
    total_cost_swords = num_toy_swords * cost_per_toy_sword

    # L3
    num_play_doughs = 10 # 10 play doughs
    cost_per_play_dough = 35 # $35 play dough
    total_cost_play_doughs = num_play_doughs * cost_per_play_dough

    # L4
    total_cost_everything = total_cost_legos + total_cost_swords + total_cost_play_doughs

    # FA
    answer = total_cost_everything
    return answer