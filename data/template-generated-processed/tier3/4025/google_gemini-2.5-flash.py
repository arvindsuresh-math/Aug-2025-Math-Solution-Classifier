def solve():
    """Index: 4025.
    Returns: the number of weeks the village will last.
    """
    # L1
    vampire_drain_rate = 3 # A vampire drains three people a week
    werewolf_eat_rate = 5 # eats five people a week
    combined_rate_per_week = vampire_drain_rate + werewolf_eat_rate

    # L2
    total_village_people = 72 # A village of 72 people
    weeks_last = total_village_people / combined_rate_per_week

    # FA
    answer = weeks_last
    return answer