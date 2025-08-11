from fractions import Fraction

def solve():
    """Index: 2667.
    Returns: the total amount of money the three friends received together.
    """
    # L1
    zachary_games_sold = 40 # Zachary sold 40 games
    price_per_game = 5 # at $5 each
    zachary_total_money = zachary_games_sold * price_per_game

    # L2
    jason_percentage_more = Fraction(30, 100) # 30% more money
    jason_additional_money = jason_percentage_more * zachary_total_money

    # L3
    jason_total_money = jason_additional_money + zachary_total_money

    # L4
    zachary_jason_combined_money = jason_total_money + zachary_total_money

    # L5
    ryan_more_than_jason = 50 # received $50 more than Jason
    ryan_total_money = jason_total_money + ryan_more_than_jason

    # L6
    total_money_three_friends = ryan_total_money + zachary_jason_combined_money

    # FA
    answer = total_money_three_friends
    return answer