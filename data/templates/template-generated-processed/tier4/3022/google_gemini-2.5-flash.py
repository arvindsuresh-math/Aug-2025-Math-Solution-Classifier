def solve():
    """Index: 3022.
    Returns: the original purchase price of the first house.
    """
    # L1
    total_percent = 100 # WK
    loan_percent = 75 # 75% he can't pay
    paid_percent_num = total_percent - loan_percent

    # L2
    new_house_cost = 500000 # new house that costs $500,000
    paid_percent_decimal = 0.25 # 25% of the new home price
    paid_towards_new_home = new_house_cost * paid_percent_decimal

    # L3
    first_house_worth_increase_factor = 1.25 # 25% more than he bought it for (1 + 0.25)
    first_house_purchase_price = paid_towards_new_home / first_house_worth_increase_factor

    # FA
    answer = first_house_purchase_price
    return answer