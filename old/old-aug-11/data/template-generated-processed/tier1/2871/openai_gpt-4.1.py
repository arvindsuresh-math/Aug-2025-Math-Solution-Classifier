def solve():
    """Index: 2871.
    Returns: the amount of money Gloria has left after buying the cabin.
    """
    # L1
    num_cypress = 20 # 20 cypress trees
    price_per_cypress = 100 # $100 for each cypress tree
    cypress_earnings = num_cypress * price_per_cypress

    # L2
    num_pine = 600 # 600 pine trees
    price_per_pine = 200 # $200 per pine tree
    pine_earnings = num_pine * price_per_pine

    # L3
    num_maple = 24 # 24 maple trees
    price_per_maple = 300 # $300 for a maple tree
    maple_earnings = num_maple * price_per_maple

    # L4
    cash_on_hand = 150 # $150 in cash
    total_money = cash_on_hand + cypress_earnings + pine_earnings + maple_earnings

    # L5
    cabin_price = 129000 # $129,000 mountain cabin
    balance = total_money - cabin_price

    # FA
    answer = balance
    return answer