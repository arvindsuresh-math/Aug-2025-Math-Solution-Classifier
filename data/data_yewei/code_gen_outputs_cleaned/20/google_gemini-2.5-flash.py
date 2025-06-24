def solve_20():
    # Number of snowflake stamps
    snowflake_stamps = 11

    # Number of truck stamps: 9 more than snowflake stamps
    truck_stamps = snowflake_stamps + 9

    # Number of rose stamps: 13 fewer than truck stamps
    rose_stamps = truck_stamps - 13

    # Total number of stamps Bella bought
    total_stamps = snowflake_stamps + truck_stamps + rose_stamps

    return total_stamps

# Call the function to get the result
# print(solve_20())