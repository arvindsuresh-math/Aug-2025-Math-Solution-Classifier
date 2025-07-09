def solve():
    total_budget = 1000
    food_percentage = 0.30
    accommodation_percentage = 0.15
    entertainment_percentage = 0.25

    # Calculate amount spent on food
    food_cost = food_percentage * total_budget

    # Calculate amount spent on accommodation
    accommodation_cost = accommodation_percentage * total_budget

    # Calculate amount spent on entertainment
    entertainment_cost = entertainment_percentage * total_budget

    # Calculate total spent on these categories
    total_spent_on_categories = food_cost + accommodation_cost + entertainment_cost

    # Calculate amount spent on coursework materials
    coursework_materials_cost = total_budget - total_spent_on_categories

    return coursework_materials_cost

# Execute the function to get the answer
answer = solve()