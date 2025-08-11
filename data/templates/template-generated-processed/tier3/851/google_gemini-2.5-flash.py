def solve():
    """Index: 851.
    Returns: the total number of rounds Jane played.
    """
    # L1
    final_points = 60 # Jane ends up with 60 points
    points_lost = 20 # she lost 20 points
    total_points_accumulated = final_points + points_lost

    # L2
    points_per_round = 10 # awarded 10 points if you win one round
    number_of_rounds = total_points_accumulated / points_per_round

    # FA
    answer = number_of_rounds
    return answer