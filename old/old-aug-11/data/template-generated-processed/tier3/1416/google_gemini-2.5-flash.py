def solve():
    """Index: 1416.
    Returns: the team's average typed words per minute.
    """
    # L1
    rudy_wpm = 64 # Rudy types 64 words per minute
    joyce_wpm = 76 # Joyce types 76 words per minute
    gladys_wpm = 91 # Gladys types 91 words per minute
    lisa_wpm = 80 # Lisa types 80 words per minute
    mike_wpm = 89 # Mike types 89 words per minute
    total_wpm = rudy_wpm + joyce_wpm + gladys_wpm + lisa_wpm + mike_wpm

    # L2
    num_employees = 5 # 5 employees
    average_wpm = total_wpm / num_employees

    # FA
    answer = average_wpm
    return answer