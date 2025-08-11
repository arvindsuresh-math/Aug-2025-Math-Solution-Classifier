def solve():
    """Index: 1517.
    Returns: the number of oranges Mark needs to pick out.
    """
    # L1
    apples = 3 # 3 apples
    bananas = 4 # 4 bananas
    current_fruit = apples + bananas

    # L2
    total_desired_fruit = 12 # 12 pieces of fruit
    oranges_needed = total_desired_fruit - current_fruit

    # FA
    answer = oranges_needed
    return answer