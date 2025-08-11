def solve():
    """Index: 1456.
    Returns: the total number of fishes caught by the team throughout the competition.
    """
    # L1
    jackson_fishes_per_day = 6 # Jackson was able to reel a total of 6 fishes per day
    competition_days = 5 # 5-day Fishing competition
    jackson_total_fishes = jackson_fishes_per_day * competition_days

    # L2
    jonah_fishes_per_day = 4 # Jonah was able to reel 4 fishes per day
    jonah_total_fishes = jonah_fishes_per_day * competition_days

    # L3
    george_fishes_per_day = 8 # George was able to reel 8 fishes per day
    george_total_fishes = george_fishes_per_day * competition_days

    # L4
    total_team_fishes = jackson_total_fishes + jonah_total_fishes + george_total_fishes

    # FA
    answer = total_team_fishes
    return answer