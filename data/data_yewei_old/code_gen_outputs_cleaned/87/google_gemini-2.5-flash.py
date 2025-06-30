def solve():
    initial_weight = 400  # pounds
    weight_multiplier = 1.5
    price_per_pound = 3  # dollars

    # Calculate the new weight of the cow
    new_weight = initial_weight * weight_multiplier

    # Calculate the weight gained
    weight_gained = new_weight - initial_weight

    # Calculate the increase in worth
    increase_in_worth = weight_gained * price_per_pound

    return increase_in_worth

# Execute the function to get the answer
# print(solve())