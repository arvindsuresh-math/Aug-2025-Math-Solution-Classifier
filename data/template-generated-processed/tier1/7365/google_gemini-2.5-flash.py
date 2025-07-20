def solve():
    """Index: 7365.
    Returns: the total money Bill has now.
    """
    # L1
    pizza_cost_per_unit = 11 # Each pizza cost $11
    num_pizzas = 3 # bought 3 large pizzas
    frank_spent_on_pizza = pizza_cost_per_unit * num_pizzas

    # L2
    frank_initial_money = 42 # Frank and Bill have $42
    frank_gives_to_bill = frank_initial_money - frank_spent_on_pizza

    # L3
    bill_initial_money = 30 # Bill had $30 already
    bill_total_money = bill_initial_money + frank_gives_to_bill

    # FA
    answer = bill_total_money
    return answer