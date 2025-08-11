def solve():
    """Index: 4819.
    Returns: the amount each remaining employee pays.
    """
    # L1
    boss_contribution = 15 # The boss agrees to contribute $15
    doubling_factor = 2 # twice as much
    todd_contribution = boss_contribution * doubling_factor

    # L2
    gift_cost = 100 # a birthday gift for Sandra that costs $100
    remaining_cost = gift_cost - todd_contribution - boss_contribution

    # L3
    num_remaining_employees = 5 # remaining 5 employees (counting Nick)
    cost_per_employee = remaining_cost / num_remaining_employees

    # FA
    answer = cost_per_employee
    return answer