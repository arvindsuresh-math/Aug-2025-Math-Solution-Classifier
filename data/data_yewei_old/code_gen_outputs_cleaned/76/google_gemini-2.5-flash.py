def solve_76():
    # Number of potatoes produced
    potatoes = 237

    # Calculate the number of cucumbers produced
    # The garden produced 60 fewer cucumbers than potatoes
    cucumbers = potatoes - 60

    # Calculate the number of peppers produced
    # The garden produced twice as many peppers as cucumbers
    peppers = cucumbers * 2

    # Calculate the total number of vegetables produced
    total_vegetables = potatoes + cucumbers + peppers

    return total_vegetables

# Execute the function to get the answer
answer = solve_76()