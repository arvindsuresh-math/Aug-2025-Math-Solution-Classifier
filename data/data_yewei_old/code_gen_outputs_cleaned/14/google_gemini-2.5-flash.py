def solve():
    pages_per_20_minutes = 8
    minutes_per_interval = 20
    total_pages_to_read = 120
    minutes_in_an_hour = 60

    # Calculate how many 20-minute intervals are in one hour
    intervals_per_hour = minutes_in_an_hour / minutes_per_interval

    # Calculate pages read per hour
    pages_per_hour = pages_per_20_minutes * intervals_per_hour

    # Calculate total hours needed to read 120 pages
    hours_needed = total_pages_to_read / pages_per_hour

    return hours_needed

# Execute the function and print the result
print(solve())