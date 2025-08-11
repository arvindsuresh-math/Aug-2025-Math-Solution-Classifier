from fractions import Fraction

def solve():
    """Index: 2292.
    Returns: the number of candies the friend can purchase.
    """
    # L1
    fraction_given = Fraction(1, 4) # one-quarter of his feeding allowance
    feeding_allowance = 4 # feeding allowance is $4
    money_given_to_friend = fraction_given * feeding_allowance

    # L3
    cents_per_dollar = 100 # WK
    candy_cost_cents = 20 # candies cost 20 cents apiece
    money_given_to_friend_cents = money_given_to_friend * cents_per_dollar
    candies_purchased = money_given_to_friend_cents / candy_cost_cents

    # FA
    answer = candies_purchased
    return answer