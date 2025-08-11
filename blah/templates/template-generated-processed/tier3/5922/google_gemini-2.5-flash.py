def solve():
    """Index: 5922.
    Returns: the total number of papers Ms. Alice can grade in 11 hours.
    """
    # L1
    total_papers = 296 # grade 296 papers
    total_hours = 8 # in 8 hours
    papers_per_hour = total_papers / total_hours

    # L2
    target_hours = 11 # in 11 hours
    total_papers_in_11_hours = papers_per_hour * target_hours

    # FA
    answer = total_papers_in_11_hours
    return answer