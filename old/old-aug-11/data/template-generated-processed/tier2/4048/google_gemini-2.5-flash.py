def solve():
    """Index: 4048.
    Returns: the total number of months Ivanka and Woody needed to write their books.
    """
    # L1
    woody_years = 1.5 # Woody spent 1.5 years writing his book
    months_per_year = 12 # WK
    woody_months = woody_years * months_per_year

    # L2
    ivanka_extra_months = 3 # took her 3 more months
    ivanka_months = woody_months + ivanka_extra_months

    # L3
    total_months = woody_months + ivanka_months

    # FA
    answer = total_months
    return answer