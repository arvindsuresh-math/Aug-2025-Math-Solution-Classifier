def solve():
    """Index: 1758.
    Returns: the number of points their teammates made.
    """
    # L1
    lizzie_score = 4 # Lizzie was able to score 4 points
    nathalie_more_than_lizzie = 3 # Nathalie's score is 3 more than Lizzie's score
    nathalie_score = lizzie_score + nathalie_more_than_lizzie

    # L2
    lizzie_nathalie_total = nathalie_score + lizzie_score

    # L3
    aimee_multiplier = 2 # Aimee's score is twice the score of Lizzie and Nathalie combined
    aimee_score = lizzie_nathalie_total * aimee_multiplier

    # L4
    lizzie_nathalie_aimee_total = aimee_score + lizzie_nathalie_total

    # L5
    team_total = 50 # the whole team was able to score 50 points
    teammates_score = team_total - lizzie_nathalie_aimee_total

    # FA
    answer = teammates_score
    return answer