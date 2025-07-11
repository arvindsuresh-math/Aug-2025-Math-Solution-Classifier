def solve():
    """Index: 1661.
    Returns: the year Tim and Donna met.
    """
    # L1
    anniversary_year = 2025 # 2025
    anniversary_duration = 20 # 20th wedding anniversary
    marriage_year = anniversary_year - anniversary_duration

    # L2
    dating_before_marriage_years = 3 # 3 years before they got married
    dating_start_year = marriage_year - dating_before_marriage_years

    # L3
    met_before_dating_years = 2 # 2 years before that
    meeting_year = dating_start_year - met_before_dating_years

    # FA
    answer = meeting_year
    return answer