def solve():
    """Index: 2281.
    Returns: the total number of single pancakes Willow will make for the girls and her son.
    """
    # L1
    num_girls = 4 # Willow’s daughter had a slumber party with 3 of her friends (daughter + 3 friends)
    servings_per_girl = 1.5 # Each of the girls wanted a serving and a half of pancakes
    total_girl_servings = num_girls * servings_per_girl

    # L2
    son_servings = 3 # Willow’s son wanted 3 servings of pancakes
    total_servings = son_servings + total_girl_servings

    # L3
    pancakes_per_serving = 4 # Willow’s pancake recipe makes 1 serving of 4 pancakes
    total_pancakes = pancakes_per_serving * total_servings

    # FA
    answer = total_pancakes
    return answer