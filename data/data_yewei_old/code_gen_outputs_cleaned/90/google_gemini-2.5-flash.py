def solve():
    # Number of days in December
    days_december = 31
    # Number of days in January
    days_january = 31
    # Number of days in February
    days_february = 28

    # Calculate the total number of days Herman feeds the birds
    total_days = days_december + days_january + days_february

    # Amount of food fed in the morning
    food_morning = 0.5 # cups
    # Amount of food fed in the afternoon
    food_afternoon = 0.5 # cups

    # Calculate the total amount of food fed per day
    food_per_day = food_morning + food_afternoon

    # Calculate the total cups of food needed for all three months
    total_food_needed = food_per_day * total_days

    return total_food_needed

# Execute the function to get the answer
answer = solve()