def solve():
    """Index: 1181.
    Returns: the total amount of money the workers received altogether.
    """
    # L1
    hours_day1 = 10 # 10 hours on the first day
    hours_day2 = 8 # 8 hours on the second day
    hours_first_two_days = hours_day1 + hours_day2

    # L2
    hours_day3 = 15 # 15 hours
    total_hours_per_worker = hours_first_two_days + hours_day3

    # L3
    pay_per_hour = 10 # $10 per hour of work
    pay_per_worker = total_hours_per_worker * pay_per_hour

    # L4
    num_workers = 2 # 2 men
    total_amount_received = pay_per_worker * num_workers

    # FA
    answer = total_amount_received
    return answer