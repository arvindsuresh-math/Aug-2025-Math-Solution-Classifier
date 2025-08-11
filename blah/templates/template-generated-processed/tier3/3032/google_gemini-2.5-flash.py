from fractions import Fraction

def solve():
    """Index: 3032.
    Returns: the remaining amount of tomatoes after giving some away.
    """
    # L1
    fraction_half = Fraction(1, 2) # half as much on Thursday
    wednesday_harvest = 400 # harvests 400 kg on Wednesday
    thursday_harvest = fraction_half * wednesday_harvest

    # L2
    total_harvest = 2000 # harvests a total of 2000 kg on Wednesday, Thursday, and Friday
    friday_harvest = total_harvest - wednesday_harvest - thursday_harvest

    # L3
    given_away_tomatoes = 700 # gives away 700kg of them to his friends
    remaining_tomatoes = friday_harvest - given_away_tomatoes

    # FA
    answer = remaining_tomatoes
    return answer