from fractions import Fraction

def solve():
    """Index: 1187.
    Returns: the maximum number of apples Brian can buy.
    """
    # L1
    subway_fare_one_way = 3.50 # pay the $3.50 subway fare each way
    total_subway_fare = subway_fare_one_way + subway_fare_one_way

    # L2
    kiwi_cost = 10 # spent $10 on kiwis
    banana_fraction = Fraction(1, 2) # half that much on bananas
    banana_cost = banana_fraction * kiwi_cost

    # L3
    total_spent_so_far = total_subway_fare + banana_cost + kiwi_cost

    # L4
    initial_money = 50 # left his house with only $50
    money_left_for_apples = initial_money - total_spent_so_far

    # L5
    cost_per_bag_apples = 14 # A bag of dozen apples costs $14
    num_bags_apples = money_left_for_apples / cost_per_bag_apples

    # L6
    apples_per_dozen = 12 # WK
    total_apples = apples_per_dozen * num_bags_apples

    # FA
    answer = total_apples
    return answer