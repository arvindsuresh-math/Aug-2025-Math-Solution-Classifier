def solve_4():
    # Number of pages per letter
    pages_per_letter = 3
    
    # Number of friends James writes to
    num_friends = 2
    
    # Number of times he writes per week
    times_per_week = 2
    
    # Number of weeks in a year
    weeks_per_year = 52

    # Calculate pages written per friend per week
    pages_per_friend_per_week = pages_per_letter * times_per_week
    
    # Calculate total pages written per week for all friends
    total_pages_per_week = pages_per_friend_per_week * num_friends
    
    # Calculate total pages written per year
    total_pages_per_year = total_pages_per_week * weeks_per_year
    
    return total_pages_per_year