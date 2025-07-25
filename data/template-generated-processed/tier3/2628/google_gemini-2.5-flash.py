def solve():
    """Index: 2628.
    Returns: the total number of wings all the birds had.
    """
    # L1
    num_grandparents = 4 # 4 grandparents
    money_per_grandparent = 50 # 50 dollars from each of his 4 grandparents
    total_money = num_grandparents * money_per_grandparent

    # L2
    cost_per_bird = 20 # each bird costs $20
    num_birds = total_money / cost_per_bird

    # L3
    wings_per_bird = 2 # Since each bird has 2 wings
    total_wings = num_birds * wings_per_bird

    # FA
    answer = total_wings
    return answer