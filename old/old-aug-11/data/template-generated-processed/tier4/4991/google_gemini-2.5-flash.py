def solve():
    """Index: 4991.
    Returns: the smallest percentage of the female vote June must receive to win.
    """
    # L1
    total_students = 200 # 200 students in the school
    win_percentage_decimal = 0.5 # 50% of the vote
    votes_for_50_percent = total_students * win_percentage_decimal

    # L2
    one_vote_more = 1 # WK
    votes_to_win = votes_for_50_percent + one_vote_more

    # L3
    boys_percentage_decimal = 0.6 # 60% of students are boys
    num_boys = total_students * boys_percentage_decimal

    # L4
    num_girls = total_students - num_boys

    # L5
    male_vote_percentage_decimal = 0.675 # 67.5% of male vote
    votes_from_boys = num_boys * male_vote_percentage_decimal

    # L6
    votes_needed_from_girls = votes_to_win - votes_from_boys

    # L7
    proportion_girls_votes = votes_needed_from_girls / num_girls

    # L8
    percentage_multiplier = 100 # WK
    female_vote_percentage_needed = percentage_multiplier * proportion_girls_votes

    # FA
    answer = female_vote_percentage_needed
    return answer