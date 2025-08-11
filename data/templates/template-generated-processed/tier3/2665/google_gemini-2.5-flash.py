def solve():
    """Index: 2665.
    Returns: the total number of fish Paul caught.
    """
    # L1
    fish_per_interval = 5 # 5 fish
    total_fishing_hours = 12 # 12 hours
    hours_per_interval = 2 # 2 hours
    number_of_intervals = total_fishing_hours // hours_per_interval

    # L2
    total_fish_caught = number_of_intervals * fish_per_interval

    # FA
    answer = total_fish_caught
    return answer