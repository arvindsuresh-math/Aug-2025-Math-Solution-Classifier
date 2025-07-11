def solve():
    """Index: 1919.
    Returns: the amount of money Roger still owes on his house.
    """
    # L1
    house_price = 100000 # bought a house for $100,000
    down_payment_percent = 0.20 # pay 20% down
    down_payment = house_price * down_payment_percent

    # L2
    remaining_after_down = house_price - down_payment

    # L3
    parents_payment_percent = 0.30 # parents paid off an additional 30%
    parents_payment = remaining_after_down * parents_payment_percent

    # L4
    amount_owed = remaining_after_down - parents_payment

    # FA
    answer = amount_owed
    return answer