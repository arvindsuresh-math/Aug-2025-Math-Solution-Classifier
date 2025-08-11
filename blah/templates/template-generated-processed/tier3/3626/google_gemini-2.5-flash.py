def solve():
    """Index: 3626.
    Returns: the total number of machines in the launderette.
    """
    # L1
    quarters_per_machine = 80 # 80 quarters
    quarters_per_dollar = 4 # WK
    money_from_quarters = quarters_per_machine / quarters_per_dollar

    # L2
    dimes_per_machine = 100 # 100 dimes
    dimes_per_dollar = 10 # WK
    money_from_dimes = dimes_per_machine / dimes_per_dollar

    # L3
    total_money_per_machine = money_from_quarters + money_from_dimes

    # L4
    total_income = 90 # total of $90
    number_of_machines = total_income / total_money_per_machine

    # FA
    answer = number_of_machines
    return answer