def solve():
    """Index: 214.
    Returns: the number of months ago Bella and Bob celebrated their 2nd anniversary.
    """
    # L1
    anniversary_years = 4 # 4th anniversary
    months_per_year = 12 # WK
    months_at_4th = anniversary_years * months_per_year

    # L2
    months_until_4th = 6 # in 6 months
    current_months = months_at_4th - months_until_4th

    # L3
    second_anniv_years = 2 # 2nd anniversary
    months_at_2nd = second_anniv_years * months_per_year

    # L4
    months_ago = current_months - months_at_2nd

    # FA
    answer = months_ago
    return answer