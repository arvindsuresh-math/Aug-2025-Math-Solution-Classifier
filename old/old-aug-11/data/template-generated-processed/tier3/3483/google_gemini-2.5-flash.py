def solve():
    """Index: 3483.
    Returns: the total amount of money collected.
    """
    # L1
    households_per_day = 20 # visits 20 households a day
    giving_households_divisor = 2 # half of those households
    giving_households_per_day = households_per_day / giving_households_divisor

    # L2
    number_of_days = 5 # for 5 days
    total_giving_households = giving_households_per_day * number_of_days

    # L3
    bill_value = 20 # a pair of 20s
    number_of_bills = 2 # a pair of 20s
    money_per_household = bill_value * number_of_bills

    # L4
    total_money_collected = money_per_household * total_giving_households

    # FA
    answer = total_money_collected
    return answer