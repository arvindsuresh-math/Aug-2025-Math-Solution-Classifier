def solve():
    """Index: 800.
    Returns: the amount of change Sandy receives back for a twenty-dollar bill.
    """
    # L1
    num_cappuccinos = 3 # she orders three cappuccinos
    price_cappuccino = 2 # cappuccinos cost $2
    total_cappuccino = num_cappuccinos * price_cappuccino

    # L2
    num_iced_teas = 2 # two iced teas
    price_iced_tea = 3 # iced teas cost $3
    total_iced_tea = num_iced_teas * price_iced_tea

    # L3
    num_cafe_lattes = 2 # two cafe lattes
    price_cafe_latte = 1.5 # cafe lattes cost $1.5
    total_cafe_latte = num_cafe_lattes * price_cafe_latte

    # L4
    num_espressos = 2 # two espressos
    price_espresso = 1 # espressos cost $1
    total_espresso = num_espressos * price_espresso

    # L5
    total_paid = total_cappuccino + total_iced_tea + total_cafe_latte + total_espresso

    # L6
    bill_amount = 20 # for a twenty-dollar bill
    change = bill_amount - total_paid

    # FA
    answer = change
    return answer