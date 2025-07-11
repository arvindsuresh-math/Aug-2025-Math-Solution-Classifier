def solve():
    """Index: 1522.
    Returns: the number of eggs the baker will need to use.
    """
    # L1
    flour_to_use = 6 # 6 cups of flour he has remaining
    recipe_flour = 2 # 2 cups of flour
    times_normal_amount = flour_to_use / recipe_flour

    # L2
    recipe_eggs = 3 # 3 eggs
    total_eggs_needed = recipe_eggs * times_normal_amount

    # FA
    answer = total_eggs_needed
    return answer