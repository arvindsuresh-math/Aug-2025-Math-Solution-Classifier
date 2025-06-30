# Leo's assignment time calculation
def solve_56():
    # Time taken for the first part of the assignment in minutes
    time_part1 = 25
    
    # Time taken for the second part is twice the first part
    time_part2 = time_part1 * 2
    
    # Total time for the assignment in hours
    total_time_hours = 2
    
    # Convert total time to minutes
    total_time_minutes = total_time_hours * 60
    
    # Calculate the combined time for the first two parts
    time_part1_and_part2 = time_part1 + time_part2
    
    # Calculate the time taken for the third part
    time_part3 = total_time_minutes - time_part1_and_part2
    
    return time_part3