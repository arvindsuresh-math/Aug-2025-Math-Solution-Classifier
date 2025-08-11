from fractions import Fraction

def solve():
    """Index: 162.
    Returns: the total amount Daniel spent on all the games in his collection.
    """
    # L1
    games_at_12 = 80 # 80 of them, Daniel bought for $12 each
    price_12 = 12 # $12 each
    spent_12 = games_at_12 * price_12

    # L2
    total_games = 346 # Daniel has a collection of 346 video games
    rest_games = total_games - games_at_12

    # L3
    percent_7 = Fraction(50, 100) # 50% were bought for $7
    games_at_7 = percent_7 * rest_games

    # L4
    price_7 = 7 # $7 each
    spent_7 = games_at_7 * price_7

    # L5
    games_at_3 = rest_games - games_at_7
    price_3 = 3 # $3 each
    spent_3 = games_at_3 * price_3

    # L6
    total_spent = spent_12 + spent_7 + spent_3

    # FA
    answer = total_spent
    return answer