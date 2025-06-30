def solve():
    # Cost of each item
    hamburger_price_per_piece = 3.0
    french_fries_price_per_set = 1.20
    soda_price_per_cup = 0.5
    spaghetti_platter_price = 2.7

    # Quantity of each item ordered
    num_hamburgers = 5
    num_french_fries_sets = 4
    num_soda_cups = 5
    num_friends = 5

    # Calculate the total cost for each item type
    cost_hamburgers = hamburger_price_per_piece * num_hamburgers
    cost_french_fries = french_fries_price_per_set * num_french_fries_sets
    cost_sodas = soda_price_per_cup * num_soda_cups

    # Calculate the total bill
    total_bill = cost_hamburgers + cost_french_fries + cost_sodas + spaghetti_platter_price

    # Calculate how much each friend will pay
    cost_per_friend = total_bill / num_friends

    return cost_per_friend

# Execute the function to get the final answer
final_answer = solve()