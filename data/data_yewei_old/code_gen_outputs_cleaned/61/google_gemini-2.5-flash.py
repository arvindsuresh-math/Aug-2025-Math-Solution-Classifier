def solve_61():
    total_weight_needed = 1000

    # Weight gained from berries (a fifth of the total)
    weight_from_berries = (1/5) * total_weight_needed

    # Weight gained from acorns (twice the amount from berries)
    weight_from_acorns = 2 * weight_from_berries

    # Weight gained so far from berries and acorns
    weight_gained_so_far = weight_from_berries + weight_from_acorns

    # Remaining weight needed before considering salmon
    remaining_weight_needed = total_weight_needed - weight_gained_so_far

    # Weight gained from salmon (half of the remaining weight)
    weight_from_salmon = remaining_weight_needed / 2

    # Weight gained from small animals (the rest of the remaining weight)
    weight_from_small_animals = remaining_weight_needed - weight_from_salmon

    return weight_from_small_animals

# Call the function to get the result
# print(solve_61())