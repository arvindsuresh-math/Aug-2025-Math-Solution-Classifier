def solve():
    """Index: 1951.
    Returns: the total number of days it takes for Marnie to eat the whole bag of chips.
    """
    # L1
    initial_chips_eaten = 5 # eats 5 of them
    additional_chips_eaten = 5 # eats 5 more
    chips_eaten_first_day = initial_chips_eaten + additional_chips_eaten

    # L2
    total_chips_in_bag = 100 # The bag has 100 chips in it
    remaining_chips_after_first_day = total_chips_in_bag - chips_eaten_first_day

    # L3
    chips_eaten_per_day = 10 # Marnie eats 10 each day
    days_to_eat_remaining_chips = remaining_chips_after_first_day / chips_eaten_per_day

    # L4
    first_day_count = 1 # on the first day she bought them
    total_days = days_to_eat_remaining_chips + first_day_count

    # FA
    answer = total_days
    return answer