def solve_67():
    # Total race distance
    total_race_distance = 30

    # Jesse's progress
    jesse_avg_first_3_days = 2 / 3
    jesse_miles_first_3_days = jesse_avg_first_3_days * 3
    jesse_miles_day_4 = 10
    
    # Calculate Jesse's remaining miles for the last 3 days
    jesse_remaining_miles = total_race_distance - jesse_miles_first_3_days - jesse_miles_day_4
    
    # Calculate Jesse's average daily miles needed for the last 3 days
    num_final_days = 3
    jesse_avg_final_3_days = jesse_remaining_miles / num_final_days

    # Mia's progress
    mia_avg_first_4_days = 3
    mia_miles_first_4_days = mia_avg_first_4_days * 4
    
    # Calculate Mia's remaining miles for the last 3 days
    mia_remaining_miles = total_race_distance - mia_miles_first_4_days
    
    # Calculate Mia's average daily miles needed for the last 3 days
    mia_avg_final_3_days = mia_remaining_miles / num_final_days

    # Calculate the total of their required averages for the final 3 days
    total_required_avg = jesse_avg_final_3_days + mia_avg_final_3_days
    
    # Calculate the average of their required averages
    average_of_averages = total_required_avg / 2

    return average_of_averages

# Execute the function to get the final answer
final_answer = solve_67()