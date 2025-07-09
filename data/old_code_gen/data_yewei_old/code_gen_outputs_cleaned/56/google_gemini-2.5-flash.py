def solve_56():
    # Time taken for the first part of the assignment in minutes
    time_part1_minutes = 25

    # Time taken for the second part of the assignment is twice the first part
    time_part2_minutes = time_part1_minutes * 2

    # Total time taken for the first two parts
    time_parts1_and_2_minutes = time_part1_minutes + time_part2_minutes

    # Total time for the entire assignment in hours
    total_assignment_time_hours = 2
    # Convert total assignment time to minutes
    total_assignment_time_minutes = total_assignment_time_hours * 60

    # Time taken for the third part of the assignment
    time_part3_minutes = total_assignment_time_minutes - time_parts1_and_2_minutes

    return time_part3_minutes

# Run the function to get the result
# print(solve_56())