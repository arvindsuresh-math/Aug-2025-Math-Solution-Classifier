def solve_86():
    """
    Calculates the number of ounces of soda Peter bought.

    Peter starts with $2, leaves with $0.50, and soda costs $0.25 per ounce.
    """
    initial_money = 2.00
    money_left = 0.50
    cost_per_ounce = 0.25

    # L1: Calculate the total amount of money Peter spent on soda.
    money_spent = initial_money - money_left

    # L2: Calculate the number of ounces of soda he bought.
    ounces_bought = money_spent / cost_per_ounce

    return ounces_bought

# Execute the function to get the final answer
final_answer = solve_86()