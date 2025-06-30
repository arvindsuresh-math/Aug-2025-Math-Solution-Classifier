def solve():
    # Cost of 2 pounds of cheddar cheese
    cheddar_cheese_cost = 10

    # Cost of cream cheese is half the price of the cheddar cheese
    cream_cheese_cost = cheddar_cheese_cost / 2

    # Cost of cold cuts is twice the price of the cheddar cheese
    cold_cuts_cost = cheddar_cheese_cost * 2

    # Total cost of all ingredients
    total_cost = cheddar_cheese_cost + cream_cheese_cost + cold_cuts_cost

    return total_cost

# Execute the function to get the answer
answer = solve()