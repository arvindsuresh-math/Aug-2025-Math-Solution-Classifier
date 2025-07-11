def solve():
    """Index: 2849.
    Returns: how much more money Anna spent on lunch than on breakfast.
    """
    # L1
    bagel_cost = 0.95 # a bagel for $0.95
    orange_juice_cost = 0.85 # a glass of orange juice for $0.85
    total_breakfast_cost = bagel_cost + orange_juice_cost

    # L2
    sandwich_cost = 4.65 # $4.65 on a sandwich
    milk_cost = 1.15 # $1.15 on a carton of milk
    total_lunch_cost = sandwich_cost + milk_cost

    # L3
    difference_in_cost = total_lunch_cost - total_breakfast_cost

    # FA
    answer = difference_in_cost
    return answer