def solve():
    """Index: 4324.
    Returns: the amount of money Carmela has to give to each cousin.
    """
    # L1
    cousin_initial_money = 2 # each of her four cousins has $2
    num_cousins = 4 # her four cousins
    total_cousin_initial_money = cousin_initial_money * num_cousins

    # L2
    carmela_initial_money = 7 # Carmela has $7
    total_money_combined = carmela_initial_money + total_cousin_initial_money

    # L3
    carmela_count = 1 # WK
    total_people = carmela_count + num_cousins

    # L4
    money_per_person = total_money_combined / total_people

    # L5
    carmela_money_to_give_total = carmela_initial_money - money_per_person

    # L6
    money_per_cousin = carmela_money_to_give_total / num_cousins

    # FA
    answer = money_per_cousin
    return answer