def solve():
    """Index: 4874.
    Returns: the total number of macaroons remaining.
    """
    # L1
    initial_green_macaroons = 40 # 40 green macarons
    green_macaroons_eaten = 15 # ate 15 green macaroons
    remaining_green_macaroons = initial_green_macaroons - green_macaroons_eaten

    # L2
    multiplier_red_macaroons = 2 # twice as many red macaroons as green macaroons
    red_macaroons_eaten = green_macaroons_eaten * multiplier_red_macaroons

    # L3
    initial_red_macaroons = 50 # 50 red macaroons
    remaining_red_macaroons = initial_red_macaroons - red_macaroons_eaten

    # L4
    total_remaining_macaroons = remaining_red_macaroons + remaining_green_macaroons

    # FA
    answer = total_remaining_macaroons
    return answer