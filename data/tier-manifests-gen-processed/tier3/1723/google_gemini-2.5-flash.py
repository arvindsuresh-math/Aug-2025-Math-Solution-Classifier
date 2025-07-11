def solve():
    """Index: 1723.
    Returns: the amount of money each person gets after combining and sharing equally.
    """
    # L1
    emani_money = 150 # Emani has $150
    money_difference = 30 # Emani has $30 more money than Howard
    howard_money = emani_money - money_difference

    # L2
    total_money = howard_money + emani_money

    # L3
    num_people = 2 # share the money equally
    money_per_person = total_money / num_people

    # FA
    answer = money_per_person
    return answer