def solve():
    """Index: 3657.
    Returns: the total number of football players and cheerleaders left.
    """
    # L1
    total_football_players = 13 # 13 football players
    quit_football_players = 10 # 10 football players ... quit
    football_players_left = total_football_players - quit_football_players

    # L2
    total_cheerleaders = 16 # 16 cheerleaders
    quit_cheerleaders = 4 # 4 cheerleaders quit
    cheerleaders_left = total_cheerleaders - quit_cheerleaders

    # L3
    total_left = football_players_left + cheerleaders_left

    # FA
    answer = total_left
    return answer