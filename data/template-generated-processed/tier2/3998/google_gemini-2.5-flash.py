def solve():
    """Index: 3998.
    Returns: the total amount Tim spent on animals.
    """
    # L1
    num_goats = 3 # 3 goats
    cost_per_goat = 400 # $400 each
    total_goats_cost = num_goats * cost_per_goat

    # L2
    llama_multiplier = 2 # twice as many llamas
    num_llamas = num_goats * llama_multiplier

    # L3
    llama_cost_increase_factor = 1.5 # 50% more each (1 + 0.5)
    cost_per_llama = cost_per_goat * llama_cost_increase_factor

    # L4
    total_llamas_cost = cost_per_llama * num_llamas

    # L5
    total_cost = total_goats_cost + total_llamas_cost

    # FA
    answer = total_cost
    return answer