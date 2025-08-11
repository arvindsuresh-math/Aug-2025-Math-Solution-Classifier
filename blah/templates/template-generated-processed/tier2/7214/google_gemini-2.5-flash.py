def solve():
    """Index: 7214.
    Returns: the number of quarters Phil has left.
    """
    # L1
    pizza_cost = 2.75 # a slice of pizza for $2.75
    soda_cost = 1.50 # a soda for $1.50
    jeans_cost = 11.50 # a pair of jeans for $11.50
    total_spent = pizza_cost + soda_cost + jeans_cost

    # L2
    initial_money = 40 # started his day with $40
    money_left = initial_money - total_spent

    # L3
    quarters_per_dollar = 4 # 4 quarters in $1.00
    money_left_whole_dollars = int(money_left)
    quarters_from_dollars = money_left_whole_dollars * quarters_per_dollar

    # L5
    quarter_from_cents = 1 # 1 quarter (from 25 cents)
    total_quarters = quarters_from_dollars + quarter_from_cents

    # FA
    answer = total_quarters
    return answer