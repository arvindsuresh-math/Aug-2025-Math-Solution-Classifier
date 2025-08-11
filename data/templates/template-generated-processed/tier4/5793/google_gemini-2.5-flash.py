def solve():
    """Index: 5793.
    Returns: the total amount Samantha spends on dog toys.
    """
    # L1
    toy_cost = 12.00 # all cost $12.00 each
    discount_fraction = 0.5 # one half off
    discounted_toy_cost = toy_cost * discount_fraction

    # L2
    cost_of_two_toys = toy_cost + discounted_toy_cost

    # L3
    num_toys_bought = 4 # She buys 4 toys
    toys_per_deal = 2 # WK
    num_deals = num_toys_bought / toys_per_deal
    total_spent = num_deals * cost_of_two_toys

    # FA
    answer = total_spent
    return answer