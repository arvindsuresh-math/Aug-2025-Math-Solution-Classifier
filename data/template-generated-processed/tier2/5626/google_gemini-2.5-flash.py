def solve():
    """Index: 5626.
    Returns: the difference in votes between the winner and the loser.
    """
    # L1
    total_students = 2000 # school has 2000 students
    voter_percentage_decimal = 0.25 # only 25% of them voted
    total_voted_students = total_students * voter_percentage_decimal

    # L2
    total_percentage = 100 # WK
    winner_percentage = 55 # winner got 55% of the votes
    loser_percentage = total_percentage - winner_percentage

    # L3
    winner_percentage_decimal = 0.55 # from solution text: .55
    winner_votes = total_voted_students * winner_percentage_decimal

    # L4
    loser_percentage_decimal = 0.45 # from solution text: .45
    loser_votes = total_voted_students * loser_percentage_decimal

    # L5
    vote_difference = winner_votes - loser_votes

    # FA
    answer = vote_difference
    return answer