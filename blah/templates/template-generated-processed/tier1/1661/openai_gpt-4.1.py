def solve():
    """Index: 1661.
    Returns: the year Tim and Donna met.
    """
    # L1
    anniversary_year = 2025 # will celebrate their 20th wedding anniversary in 2025
    years_married = 20 # 20th wedding anniversary
    marriage_year = anniversary_year - years_married

    # L2
    years_dating_before_marriage = 3 # started dating 3 years before they got married
    dating_year = marriage_year - years_dating_before_marriage

    # L3
    years_met_before_dating = 2 # met 2 years before that
    met_year = dating_year - years_met_before_dating

    # FA
    answer = met_year
    return answer