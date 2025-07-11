def solve_23():
    # Given values
    total_spent = 75
    num_shorts = 5
    price_per_short = 7
    num_shoes = 2
    price_per_shoe = 10
    num_tops = 4

    # Calculate the total cost of shorts
    cost_shorts = num_shorts * price_per_short

    # Calculate the total cost of shoes
    cost_shoes = num_shoes * price_per_shoe

    # Calculate the combined cost of shorts and shoes
    combined_cost_shorts_shoes = cost_shorts + cost_shoes

    # Calculate the total cost of the tops
    cost_tops = total_spent - combined_cost_shorts_shoes

    # Calculate the cost of each top
    cost_per_top = cost_tops / num_tops

    return cost_per_top

# Execute the function to get the answer
# print(solve_23())