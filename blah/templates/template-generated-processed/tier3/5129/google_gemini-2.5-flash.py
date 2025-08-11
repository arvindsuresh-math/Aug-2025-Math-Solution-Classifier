from fractions import Fraction

def solve():
    """Index: 5129.
    Returns: the total number of fruits Karlee is left with.
    """
    # L1
    initial_grapes = 100 # Karlee has 100 grapes
    strawberry_fraction = Fraction(3, 5) # 3/5 as many strawberries as grapes
    initial_strawberries = strawberry_fraction * initial_grapes

    # L2
    fruit_share_per_friend = Fraction(1, 5) # 1/5 of each fruit
    grapes_given_per_friend = fruit_share_per_friend * initial_grapes

    # L3
    number_of_friends = 2 # two of her friends
    total_grapes_given = number_of_friends * grapes_given_per_friend

    # L4
    remaining_grapes = initial_grapes - total_grapes_given

    # L5
    strawberries_given_per_friend = fruit_share_per_friend * initial_strawberries

    # L6
    total_strawberries_given = number_of_friends * strawberries_given_per_friend

    # L7
    remaining_strawberries = initial_strawberries - total_strawberries_given

    # L8
    total_remaining_fruits = remaining_strawberries + remaining_grapes

    # FA
    answer = total_remaining_fruits
    return answer