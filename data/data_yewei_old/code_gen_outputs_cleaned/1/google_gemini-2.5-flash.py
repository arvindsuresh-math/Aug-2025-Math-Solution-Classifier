def solve_1():
    hourly_rate = 12  # dollars per hour
    minutes_worked = 50  # minutes

    # Convert hourly rate to per-minute rate
    minutes_per_hour = 60
    rate_per_minute = hourly_rate / minutes_per_hour

    # Calculate total earnings
    total_earnings = rate_per_minute * minutes_worked

    return total_earnings

# Execute the function to get the answer
# print(solve_1())