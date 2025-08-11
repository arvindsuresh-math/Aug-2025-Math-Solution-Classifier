def solve():
    """Index: 307.
    Returns: the number of calories remaining in the block.
    """
    # L1
    servings_per_block = 16 # Rick buys the large blocks that have 16 servings per block
    servings_eaten = 5 # Rick has already eaten 5 servings of cheese
    remaining_servings = servings_per_block - servings_eaten

    # L2
    calories_per_serving = 110 # 110 calories in a serving of cheese
    remaining_calories = remaining_servings * calories_per_serving

    # FA
    answer = remaining_calories
    return answer