def solve():
    """Index: 4847.
    Returns: the amount Lucy will pay in dollars.
    """
    # L1
    num_people = 10 # Ten people will be at the party
    chips_per_person = 1.2 # each person to get 1.2 pounds
    total_pounds = num_people * chips_per_person

    # L2
    cents_per_pound = 25 # 25 cents per pound
    total_cents = total_pounds * cents_per_pound

    # L3
    cents_per_dollar = 100 # WK
    total_dollars = total_cents / cents_per_dollar

    # FA
    answer = total_dollars
    return answer