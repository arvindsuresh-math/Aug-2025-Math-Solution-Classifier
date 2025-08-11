def solve():
    """Index: 5472.
    Returns: the total earnings for the week from repairs.
    """
    # L1
    phone_repair_cost = 11 # phone repair costs $11
    num_phone_repairs = 5 # 5 phone repairs
    earned_phone_repairs = phone_repair_cost * num_phone_repairs

    # L2
    laptop_repair_cost = 15 # laptop repair costs $15
    num_laptop_repairs = 2 # 2 laptop repairs
    earned_laptop_repairs = laptop_repair_cost * num_laptop_repairs

    # L3
    computer_repair_cost = 18 # computer repair costs $18
    num_computer_repairs = 2 # 2 computer repairs
    earned_computer_repairs = computer_repair_cost * num_computer_repairs

    # L4
    total_earnings = earned_phone_repairs + earned_laptop_repairs + earned_computer_repairs

    # FA
    answer = total_earnings
    return answer