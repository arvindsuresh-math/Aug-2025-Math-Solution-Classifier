def solve():
    """Index: 307.
    Returns: the number of calories remaining in the block of cheese.
    """
    # L1
    servings_per_block = 16 # large blocks that have 16 servings per block
    servings_eaten = 5 # Rick has already eaten 5 servings
    servings_left = servings_per_block - servings_eaten

    # L2
    calories_per_serving = 110 # 110 calories in a serving of cheese
    calories_remaining = servings_left * calories_per_serving

    # FA
    answer = calories_remaining
    return answer