def solve():
    """Index: 4401.
    Returns: how much Alice is short or above her goal.
    """
    # L1
    num_nikes_sold = 8 # sells 8 Nikes
    nike_cost = 60 # Nike cost $60
    total_nike_sales = num_nikes_sold * nike_cost

    # L2
    num_adidas_sold = 6 # 6 Adidas's
    adidas_cost = 45 # Adidas cost $45
    total_adidas_sales = num_adidas_sold * adidas_cost

    # L3
    num_reeboks_sold = 9 # 9 Reeboks
    reebok_cost = 35 # Reeboks cost $35
    total_reebok_sales = num_reeboks_sold * reebok_cost

    # L4
    total_sales = total_nike_sales + total_adidas_sales + total_reebok_sales

    # L5
    quota = 1000 # sell $1000 of shoes to meet her quota
    short_or_above_goal = total_sales - quota

    # FA
    answer = short_or_above_goal
    return answer