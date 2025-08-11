def solve():
    """Index: 3045.
    Returns: the number of tickets left unsold.
    """
    # L1
    num_rolls = 30 # 30 rolls of tickets
    tickets_per_roll = 100 # Each roll of tickets has 100 tickets
    total_tickets_ordered = num_rolls * tickets_per_roll

    # L2
    fourth_graders_percentage_numerator = 30 # 30% of the tickets
    percentage_denominator = 100 # 30% of the tickets
    tickets_bought_by_fourth_graders = total_tickets_ordered * fourth_graders_percentage_numerator / percentage_denominator

    # L3
    tickets_left_after_fourth_graders = total_tickets_ordered - tickets_bought_by_fourth_graders

    # L4
    fifth_graders_percentage_numerator = 50 # 50% of the remaining tickets
    tickets_bought_by_fifth_graders = tickets_left_after_fourth_graders * fifth_graders_percentage_numerator / percentage_denominator

    # L5
    tickets_left_after_fifth_graders = tickets_left_after_fourth_graders - tickets_bought_by_fifth_graders

    # L6
    tickets_bought_by_sixth_graders = 100 # 6th graders bought a total of 100 tickets
    tickets_left_unsold = tickets_left_after_fifth_graders - tickets_bought_by_sixth_graders

    # FA
    answer = tickets_left_unsold
    return answer