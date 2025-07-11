from fractions import Fraction

def solve():
    """Index: 2168.
    Returns: the amount the president saved for the presidency.
    """
    # L1
    friends_percentage = Fraction(40, 100) # 40% of this amount
    total_campaign_funds = 10000 # $10,000 in campaign funds
    friends_contribution = friends_percentage * total_campaign_funds

    # L2
    remaining_after_friends = total_campaign_funds - friends_contribution

    # L3
    family_percentage = Fraction(30, 100) # 30% of the remaining amount
    family_contribution = family_percentage * remaining_after_friends

    # L4
    own_savings = remaining_after_friends - family_contribution

    # FA
    answer = own_savings
    return answer