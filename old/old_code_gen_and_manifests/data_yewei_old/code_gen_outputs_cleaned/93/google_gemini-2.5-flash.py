def solve_93():
    # Beef details
    beef_pounds = 1000
    beef_price_per_pound = 8
    
    # Calculate the cost of beef
    cost_of_beef = beef_pounds * beef_price_per_pound
    
    # Chicken details
    # He orders twice the amount of beef in chicken
    chicken_pounds = beef_pounds * 2
    chicken_price_per_pound = 3
    
    # Calculate the cost of chicken
    cost_of_chicken = chicken_pounds * chicken_price_per_pound
    
    # Calculate the total cost
    total_cost = cost_of_beef + cost_of_chicken
    
    return total_cost

# Execute the function to get the answer
# print(solve_93())