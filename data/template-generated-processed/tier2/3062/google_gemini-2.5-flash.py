def solve():
    """Index: 3062.
    Returns: the total pints of vegetables and broth needed for 8 servings.
    """
    # L1
    vegetables_per_serving = 1 # 1 cup of vegetables
    broth_per_serving = 2.5 # 2.5 cups of broth
    total_cups_per_serving = vegetables_per_serving + broth_per_serving

    # L2
    num_servings = 8 # 8 servings
    total_cups_needed = num_servings * total_cups_per_serving

    # L3
    cups_per_pint = 2 # WK
    total_pints_needed = total_cups_needed / cups_per_pint

    # FA
    answer = total_pints_needed
    return answer