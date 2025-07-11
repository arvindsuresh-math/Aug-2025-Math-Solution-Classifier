def solve():
    """Index: 493.
    Returns: the total money used to pay for the party expenses.
    """
    # L1
    cost_per_attendee = 100 # each attendee had to pay $100
    num_attendees = 50 # 50 people at the party
    total_contributions = cost_per_attendee * num_attendees

    # L2
    expenses_less_than_contributions = 500 # $500 less than the total contributions
    total_expenses = total_contributions - expenses_less_than_contributions

    # FA
    answer = total_expenses
    return answer