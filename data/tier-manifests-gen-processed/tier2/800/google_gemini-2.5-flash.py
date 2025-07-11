def solve():
    """Index: 800.
    Returns: the amount of change Sandy receives back.
    """
    # L1
    num_cappuccinos = 3 # three cappuccinos
    cost_per_cappuccino = 2 # Cappuccinos cost $2
    total_cappuccino_cost = num_cappuccinos * cost_per_cappuccino

    # L2
    num_iced_teas = 2 # two iced teas
    cost_per_iced_tea = 3 # iced teas cost $3
    total_iced_tea_cost = num_iced_teas * cost_per_iced_tea

    # L3
    num_cafe_lattes = 2 # two cafe lattes
    cost_per_cafe_latte = 1.5 # cafe lattes cost $1.5
    total_cafe_latte_cost = num_cafe_lattes * cost_per_cafe_latte

    # L4
    num_espressos = 2 # two espressos
    cost_per_espresso = 1 # espressos cost $1 each
    total_espresso_cost = num_espressos * cost_per_espresso

    # L5
    total_cost = total_cappuccino_cost + total_iced_tea_cost + total_cafe_latte_cost + total_espresso_cost

    # L6
    bill_amount = 20 # twenty-dollar bill
    change_received = bill_amount - total_cost

    # FA
    answer = change_received
    return answer