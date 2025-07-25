def solve_75():
    # Define the cost of each item
    cost_per_slice_toast = 1  # £
    cost_per_egg = 3          # £

    # Dale's order
    dale_toast_slices = 2
    dale_eggs = 2

    # Andrew's order
    andrew_toast_slices = 1
    andrew_eggs = 2

    # Calculate Dale's toast cost
    dale_toast_cost = dale_toast_slices * cost_per_slice_toast

    # Calculate Andrew's toast cost
    andrew_toast_cost = andrew_toast_slices * cost_per_slice_toast

    # Calculate Dale's egg cost
    dale_egg_cost = dale_eggs * cost_per_egg

    # Calculate Andrew's egg cost
    andrew_egg_cost = andrew_eggs * cost_per_egg

    # Calculate the total breakfast cost
    total_breakfast_cost = dale_toast_cost + andrew_toast_cost + dale_egg_cost + andrew_egg_cost

    return total_breakfast_cost

# Execute the function to get the answer
answer = solve_75()