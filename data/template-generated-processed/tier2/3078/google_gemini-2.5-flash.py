def solve():
    """Index: 3078.
    Returns: how many more kilograms Luca lost than Barbi.
    """
    # L1
    barbi_monthly_loss = 1.5 # lost 1.5 kilograms each month
    months_in_year = 12 # for a year
    barbi_total_loss = barbi_monthly_loss * months_in_year

    # L2
    luca_yearly_loss = 9 # lost 9 kilograms every year
    luca_years = 11 # for 11 years
    luca_total_loss = luca_yearly_loss * luca_years

    # L3
    difference_in_loss = luca_total_loss - barbi_total_loss

    # FA
    answer = difference_in_loss
    return answer