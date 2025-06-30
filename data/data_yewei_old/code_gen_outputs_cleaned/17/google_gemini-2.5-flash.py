def solve():
    # Initial number of hard hats
    initial_pink_hats = 26
    initial_green_hats = 15
    initial_yellow_hats = 24

    # Carl's actions
    carl_removed_pink = 4
    pink_hats_after_carl = initial_pink_hats - carl_removed_pink

    # John's actions
    john_removed_pink = 6
    pink_hats_after_john = pink_hats_after_carl - john_removed_pink

    john_removed_green = 2 * john_removed_pink
    green_hats_after_john = initial_green_hats - john_removed_green

    # Yellow hard hats remain unchanged
    remaining_yellow_hats = initial_yellow_hats

    # Calculate the total number of hard hats remaining
    total_remaining_hard_hats = pink_hats_after_john + green_hats_after_john + remaining_yellow_hats

    return total_remaining_hard_hats

# Execute the function to get the result
result = solve()