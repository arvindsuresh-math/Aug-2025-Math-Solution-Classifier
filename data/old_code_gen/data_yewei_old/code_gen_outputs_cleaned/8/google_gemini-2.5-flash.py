def solve_8():
    # Initial budget Alexis had
    initial_budget = 200

    # Costs of items for which Alexis has receipts
    cost_shirt = 30
    cost_suit_pants = 46
    cost_suit_coat = 38
    cost_socks = 11
    cost_belt = 18

    # Money left from the budget
    money_left = 16

    # Calculate the total cost of items with receipts
    total_known_items_cost = cost_shirt + cost_suit_pants + cost_suit_coat + cost_socks + cost_belt

    # Calculate the total amount Alexis actually spent
    total_amount_spent = initial_budget - money_left

    # Calculate the cost of the shoes
    cost_shoes = total_amount_spent - total_known_items_cost

    return cost_shoes

# Execute the function to get the answer
# print(solve_8())