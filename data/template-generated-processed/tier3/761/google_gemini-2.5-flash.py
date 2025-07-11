def solve():
    """Index: 761.
    Returns: the number of apples Joan can purchase.
    """
    # L1
    num_hummus_containers = 2 # 2 containers of hummus
    cost_per_hummus = 5 # $5 each
    total_hummus_cost = num_hummus_containers * cost_per_hummus

    # L2
    cost_chicken = 20 # chicken for $20
    cost_bacon = 10 # bacon for $10
    cost_vegetables = 10 # vegetables for $10
    total_other_groceries_cost = cost_chicken + cost_bacon + cost_vegetables

    # L3
    initial_money = 60 # total of $60 to spend
    remaining_money = initial_money - total_hummus_cost - total_other_groceries_cost

    # L4
    cost_per_apple = 2 # apples which are $2 each
    num_apples = remaining_money / cost_per_apple

    # FA
    answer = num_apples
    return answer