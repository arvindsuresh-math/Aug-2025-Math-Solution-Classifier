def solve():
    # Given values
    movie_creation_cost = 2000  # Cost to create the movie
    cost_to_make_dvd = 6        # Cost to make each DVD
    selling_price_multiplier = 2.5 # Selling price is 2.5 times the cost to make
    movies_sold_per_day = 500   # Number of movies sold per day
    days_worked_per_week = 5    # Days movies are sold per week
    number_of_weeks = 20        # Total number of weeks

    # L1: Calculate the selling price per DVD
    selling_price_per_dvd = cost_to_make_dvd * selling_price_multiplier

    # L2: Calculate the profit per DVD
    profit_per_dvd = selling_price_per_dvd - cost_to_make_dvd

    # L3: Calculate the daily profit from DVD sales
    daily_profit_from_sales = profit_per_dvd * movies_sold_per_day

    # L4: Calculate the weekly profit from DVD sales
    weekly_profit_from_sales = daily_profit_from_sales * days_worked_per_week

    # L5: Calculate the total profit from DVD sales over 20 weeks
    total_sales_profit = weekly_profit_from_sales * number_of_weeks

    # L6: Calculate the net profit after subtracting the initial movie creation cost
    net_profit = total_sales_profit - movie_creation_cost

    return net_profit

# Execute the function and print the result
# print(solve())