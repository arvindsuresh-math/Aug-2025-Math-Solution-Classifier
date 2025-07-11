def solve():
    """Index: 2849.
    Returns: how much more money Anna spent on lunch than on breakfast.
    """
    # L1
    bagel_cost = 0.95 # bagel for $0.95
    orange_juice_cost = 0.85 # orange juice for $0.85
    breakfast_total = bagel_cost + orange_juice_cost

    # L2
    sandwich_cost = 4.65 # sandwich for $4.65
    milk_cost = 1.15 # carton of milk for $1.15
    lunch_total = sandwich_cost + milk_cost

    # L3
    difference = lunch_total - breakfast_total

    # FA
    answer = difference
    return answer