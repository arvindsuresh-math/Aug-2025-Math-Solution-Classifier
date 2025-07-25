def solve():
    """Index: 4466.
    Returns: the total amount Lucas' father will pay him.
    """
    # L1
    num_floors = 3 # a 3-story house
    windows_per_floor = 3 # Each floor of Lucas' house has 3 windows
    total_windows = num_floors * windows_per_floor

    # L2
    pay_per_window = 2 # $2 for each window
    earnings_from_windows = total_windows * pay_per_window

    # L3
    days_taken = 6 # In 6 days, Lucas finishes
    deduction_interval = 3 # $1 for every 3 days
    total_deduction = days_taken / deduction_interval

    # L4
    final_payment = earnings_from_windows - total_deduction

    # FA
    answer = final_payment
    return answer