def solve():
    """Index: 1921.
    Returns: the number of weeks it takes for Lisa to eat all the candies.
    """
    # L1
    candies_per_special_day = 2 # eats 2 candies for each day
    special_days_count = 2 # On Mondays and Wednesdays
    candies_eaten_special_days = candies_per_special_day * special_days_count

    # L2
    candies_per_other_day = 1 # she eats 1 candy for each day
    other_days_count = 5 # WK
    candies_eaten_other_days = other_days_count * candies_per_other_day

    # L3
    candies_per_week = candies_eaten_other_days + candies_eaten_special_days

    # L4
    total_candies = 36 # Lisa has 36 candies
    weeks_to_eat_all_candies = total_candies / candies_per_week

    # FA
    answer = weeks_to_eat_all_candies
    return answer