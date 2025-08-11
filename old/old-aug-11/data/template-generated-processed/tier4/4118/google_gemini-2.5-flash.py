def solve():
    """Index: 4118.
    Returns: the average number of apples each guest eats.
    """
    # L1
    num_pies = 3 # She plans to make 3 pies
    servings_per_pie = 8 # each contain 8 servings
    total_servings = num_pies * servings_per_pie

    # L2
    num_guests = 12 # she has 12 quests
    servings_per_guest = total_servings / num_guests

    # L3
    apples_per_serving = 1.5 # each serving requires 1.5 apples
    apples_per_guest = servings_per_guest * apples_per_serving

    # FA
    answer = apples_per_guest
    return answer