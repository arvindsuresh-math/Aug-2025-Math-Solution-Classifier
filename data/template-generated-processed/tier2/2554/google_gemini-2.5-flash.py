def solve():
    """Index: 2554.
    Returns: the total amount Donny has to pay for all the apples.
    """
    # L1
    small_apple_cost = 1.5 # Each small apple cost $1.5
    num_small_apples = 6 # bought 6 small and medium apples
    cost_small_apples = small_apple_cost * num_small_apples

    # L2
    medium_apple_cost = 2 # medium apple cost $2
    num_medium_apples = 6 # bought 6 small and medium apples
    cost_medium_apples = medium_apple_cost * num_medium_apples

    # L3
    num_big_apples = 8 # 8 big apples
    big_apple_cost = 3 # big apples cost $3
    cost_big_apples = num_big_apples * big_apple_cost

    # L4
    total_cost = cost_small_apples + cost_medium_apples + cost_big_apples

    # FA
    answer = total_cost
    return answer