def solve():
    """Index: 2685.
    Returns: the amount of the security deposit Lana and Mike need to pay.
    """
    # L1
    days_per_week = 7 # 7 days in a week
    num_weeks = 2 # going for 2 weeks
    total_days = days_per_week * num_weeks

    # L2
    daily_rate = 125.00 # daily rate is $125.00
    rental_fee = daily_rate * total_days

    # L3
    pet_fee = 100.00 # $100.00 pet fee
    total_before_service = pet_fee + rental_fee

    # L4
    service_fee_percent_decimal = 0.20 # .20*1850
    service_fee = service_fee_percent_decimal * total_before_service

    # L5
    total_bill = total_before_service + service_fee

    # L6
    security_deposit_percent_num = 50 # 50% of the entire bill
    percent_factor = 0.01 # WK
    security_deposit = security_deposit_percent_num * percent_factor * total_bill

    # FA
    answer = security_deposit
    return answer