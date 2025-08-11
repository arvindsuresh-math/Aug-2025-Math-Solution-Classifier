def solve():
    """Index: 6260.
    Returns: the amount of money Sandra will be left with after the purchase.
    """
    # L1
    mother_gift = 4 # her mother gave her an additional $4
    father_multiplier = 2 # twice as much as her mother
    father_gift = mother_gift * father_multiplier

    # L2
    sandra_saved = 10 # She saved $10
    total_money = father_gift + mother_gift + sandra_saved

    # L3
    num_candies = 14 # 14 candies
    cost_per_candy = 0.5 # One candy costs $0.5
    cost_candies = num_candies * cost_per_candy

    # L4
    num_jellybeans = 20 # 20 jelly beans
    cost_per_jellybean = 0.2 # one jelly bean $0.2
    cost_jellybeans = num_jellybeans * cost_per_jellybean

    # L5
    money_left = total_money - cost_jellybeans - cost_candies

    # FA
    answer = money_left
    return answer