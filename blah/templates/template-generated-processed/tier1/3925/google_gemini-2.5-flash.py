def solve():
    """Index: 3925.
    Returns: the number of hours Jenny has left to write her report.
    """
    # L1
    research_hours = 10 # 10 hours doing research
    proposal_hours = 2 # 2 hours writing a proposal
    hours_spent_so_far = research_hours + proposal_hours

    # L2
    total_hours_allowed = 20 # 20 hours total to work on the project
    hours_left_for_report = total_hours_allowed - hours_spent_so_far

    # FA
    answer = hours_left_for_report
    return answer