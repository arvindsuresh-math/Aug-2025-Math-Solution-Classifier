def solve():
    """Index: 1517.
    Returns: the number of oranges Mark needs to pick out to have 12 total pieces of fruit.
    """
    # L1
    apples = 3 # already chosen 3 apples
    bananas = 4 # selected a bunch of bananas containing 4 bananas
    fruit_so_far = apples + bananas

    # L2
    total_fruit_needed = 12 # buy a total of 12 pieces of fruit
    oranges_needed = total_fruit_needed - fruit_so_far

    # FA
    answer = oranges_needed
    return answer