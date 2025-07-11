def solve():
    """Index: 1456.
    Returns: the total number of fishes caught by the team during the competition.
    """
    # L1
    jackson_per_day = 6 # Jackson was able to reel a total of 6 fishes per day
    num_days = 5 # 5-day Fishing competition
    jackson_total = jackson_per_day * num_days

    # L2
    jonah_per_day = 4 # Jonah was able to reel 4 fishes per day
    jonah_total = jonah_per_day * num_days

    # L3
    george_per_day = 8 # George was able to reel 8 fishes per day
    george_total = george_per_day * num_days

    # L4
    team_total = jackson_total + jonah_total + george_total

    # FA
    answer = team_total
    return answer