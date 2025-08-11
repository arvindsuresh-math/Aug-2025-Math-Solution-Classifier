def solve():
    """Index: 6263.
    Returns: the total number of blankets collected for donation.
    """
    # L1
    team_members = 15 # 15 people on the team
    blankets_per_person_day1 = 2 # each of them gave 2 blankets
    blankets_day1 = team_members * blankets_per_person_day1

    # L2
    multiplier_day2 = 3 # tripled the number
    blankets_day2 = blankets_day1 * multiplier_day2

    # L3
    blankets_day3 = 22 # got a total of 22 blankets
    total_blankets = blankets_day2 + blankets_day3 + blankets_day1

    # FA
    answer = total_blankets
    return answer