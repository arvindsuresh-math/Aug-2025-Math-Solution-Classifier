def solve():
    """Index: 4223.
    Returns: the average cost of each piece of fruit in dollars.
    """
    # L2
    num_apples = 12 # 12 apples
    cost_per_apple = 2 # Apples cost $2
    cost_apples = num_apples * cost_per_apple

    # L3
    num_bananas = 4 # 4 bananas
    cost_per_banana = 1 # bananas cost $1
    cost_bananas = num_bananas * cost_per_banana

    # L4
    # Note: The numbers for oranges (3 oranges, $4 per orange) are taken directly from the solution line, not the question.
    num_oranges = 3
    cost_per_orange = 4
    cost_oranges = num_oranges * cost_per_orange

    # L5
    total_cost_spent = cost_apples + cost_bananas + cost_oranges

    # L6
    total_fruits_bought = num_apples + num_bananas + num_oranges

    # L7
    average_cost_per_fruit = total_cost_spent / total_fruits_bought

    # FA
    answer = average_cost_per_fruit
    return answer