def solve():
    """Index: 493.
    Returns: the amount of money used to pay for the party expenses.
    """
    # L1
    contribution_per_person = 100 # each attendee had to pay $100
    num_attendees = 50 # 50 people at the party
    total_contributions = contribution_per_person * num_attendees

    # L2
    difference_expenses_contributions = 500 # total expenses were $500 less than the total contributions
    total_expenses = total_contributions - difference_expenses_contributions

    # FA
    answer = total_expenses
    return answer