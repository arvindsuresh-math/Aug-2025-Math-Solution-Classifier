def solve():
    """Index: 6921.
    Returns: the amount of money Yanni had left in cents.
    """
    # L1
    initial_money = 0.85 # Yanni has $0.85
    money_from_mother = 0.40 # His mother gave him $0.40
    money_after_mother = money_from_mother + initial_money

    # L2
    money_found = 0.50 # Yanni found $0.50
    total_money_before_toy = money_after_mother + money_found

    # L3
    toy_cost = 1.6 # He bought a toy that cost $1.6
    money_left_dollars = total_money_before_toy - toy_cost

    # L4
    cents_per_dollar = 100 # WK
    money_left_cents = cents_per_dollar * money_left_dollars

    # FA
    answer = money_left_cents
    return answer