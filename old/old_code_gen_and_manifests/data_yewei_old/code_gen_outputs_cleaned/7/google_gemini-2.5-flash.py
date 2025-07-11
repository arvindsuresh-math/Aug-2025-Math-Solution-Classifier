def solve():
    # Initial weight of the box after adding the first batch of jelly beans
    initial_weight_jelly_beans = 2  # pounds

    # After adding brownies, the weight triples
    weight_after_brownies = initial_weight_jelly_beans * 3

    # After adding another 2 pounds of jelly beans
    weight_after_more_jelly_beans = weight_after_brownies + 2

    # After adding gummy worms, the weight doubles again
    final_weight = weight_after_more_jelly_beans * 2

    return final_weight

# Execute the function to get the final answer
final_answer = solve()