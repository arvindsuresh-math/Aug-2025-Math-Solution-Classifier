def solve():
    """Index: 1187.
    Returns: the maximum number of apples Brian can buy.
    """
    # L1
    subway_fare_one_way = 3.5 # $3.50 subway fare each way
    subway_fare_total = subway_fare_one_way + subway_fare_one_way

    # L2
    kiwi_spent = 10 # $10 on kiwis
    banana_fraction = 0.5 # half that much on bananas
    banana_spent = banana_fraction * kiwi_spent

    # L3
    total_spent_so_far = subway_fare_total + banana_spent + kiwi_spent

    # L4
    initial_money = 50 # left his house with only $50
    money_left_for_apples = initial_money - total_spent_so_far

    # L5
    bag_cost = 14 # bag of dozen apples costs $14
    max_bags = money_left_for_apples / bag_cost

    # L6
    apples_per_bag = 12 # dozen (12) apples per bag
    max_apples = int(max_bags) * apples_per_bag

    # FA
    answer = max_apples
    return answer