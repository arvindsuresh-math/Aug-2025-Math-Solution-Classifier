def solve():
    """Index: 6788.
    Returns: the amount of money Roberta has left after purchases.
    """
    # L1
    shoes_cost = 45 # spends $45 on new shoes
    bag_discount = 17 # $17 less on a new bag
    bag_cost = shoes_cost - bag_discount

    # L2
    lunch_divisor = 4 # a quarter of the price of the bag
    lunch_cost = bag_cost / lunch_divisor

    # L3
    total_spent = shoes_cost + bag_cost + lunch_cost

    # L4
    initial_money = 158 # takes $158 with her
    money_left = initial_money - total_spent

    # FA
    answer = money_left
    return answer