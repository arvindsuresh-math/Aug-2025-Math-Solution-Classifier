def solve():
    """Index: 3274.
    Returns: the number of fish in the aquarium when James discovers the Bobbit worm.
    """
    # L1
    initial_weeks_prey = 2 # After two weeks
    additional_weeks_prey = 1 # A week later
    total_weeks_prey = initial_weeks_prey + additional_weeks_prey

    # L2
    days_per_week = 7 # WK
    total_days_prey = total_weeks_prey * days_per_week

    # L3
    fish_eaten_per_day = 2 # eats 2 fish
    total_fish_eaten = total_days_prey * fish_eaten_per_day

    # L4
    initial_fish = 60 # 60 fish to start with
    fish_added = 8 # adds 8 more fish
    fish_before_eating = initial_fish + fish_added

    # L5
    surviving_fish = fish_before_eating - total_fish_eaten

    # FA
    answer = surviving_fish
    return answer