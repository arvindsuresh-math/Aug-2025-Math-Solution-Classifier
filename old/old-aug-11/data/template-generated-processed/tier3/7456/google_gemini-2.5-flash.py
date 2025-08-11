def solve():
    """Index: 7456.
    Returns: the total amount Mary will pay for the fruits.
    """
    # L1
    num_apples = 5 # Mary buys 5 apples
    cost_apple = 1 # Apples cost $1
    cost_apples = num_apples * cost_apple

    # L2
    num_oranges = 3 # 3 oranges
    cost_orange = 2 # oranges cost $2
    cost_oranges = num_oranges * cost_orange

    # L3
    num_bananas = 2 # 2 bananas
    cost_banana = 3 # bananas cost $3
    cost_bananas = num_bananas * cost_banana

    # L4
    total_fruits = num_apples + num_oranges + num_bananas

    # L5
    fruits_for_discount = 5 # For every 5 fruits
    total_discount = total_fruits / fruits_for_discount

    # L6
    subtotal_bill = cost_apples + cost_oranges + cost_bananas

    # L7
    final_payment = subtotal_bill - total_discount

    # FA
    answer = final_payment
    return answer