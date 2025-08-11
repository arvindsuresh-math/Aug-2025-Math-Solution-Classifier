def solve():
    """Index: 6392.
    Returns: the total amount Ariana owes.
    """
    # L1
    bill1_amount = 200 # The first bill for $200
    bill1_interest_rate_percent = 10 # charges 10% simple interest
    percent_to_decimal_factor = 0.01 # WK
    bill1_monthly_late_fee = bill1_amount * bill1_interest_rate_percent * percent_to_decimal_factor

    # L2
    bill1_overdue_months = 2 # it's 2 months overdue
    bill1_total_late_fee = bill1_monthly_late_fee * bill1_overdue_months

    # L3
    bill2_flat_late_fee_per_month = 50 # charges a flat $50 late fee per month
    bill2_overdue_months = 6 # is 6 months overdue
    bill2_total_late_fee = bill2_flat_late_fee_per_month * bill2_overdue_months

    # L4
    bill3_first_month_fee = 40 # charges a $40 fee the first month overdue
    bill3_second_month_fee_multiplier = 2 # twice that fee the second month overdue
    bill3_second_month_late_fee = bill3_second_month_fee_multiplier * bill3_first_month_fee

    # L5
    bill2_original_amount = 130 # The second bill for $130
    bill3_original_amount = 444 # The last bill is for $444
    total_amount_owed = bill1_total_late_fee + bill1_amount + bill2_total_late_fee + bill2_original_amount + bill3_first_month_fee + bill3_second_month_late_fee + bill3_original_amount

    # FA
    answer = total_amount_owed
    return answer