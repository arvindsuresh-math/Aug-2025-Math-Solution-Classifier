def solve():
    """Index: 2281.
    Returns: the total number of single pancakes Willow will make.
    """
    # L1
    total_girls = 4 # daughter had a slumber party with 3 of her friends
    servings_per_girl = 1.5 # a serving and a half of pancakes
    girls_total_servings = total_girls * servings_per_girl

    # L2
    son_servings = 3 # Willow’s son wanted 3 servings of pancakes
    total_servings_needed = son_servings + girls_total_servings

    # L3
    pancakes_per_serving = 4 # makes 1 serving of 4 pancakes
    total_pancakes = pancakes_per_serving * total_servings_needed

    # FA
    answer = total_pancakes
    return answer