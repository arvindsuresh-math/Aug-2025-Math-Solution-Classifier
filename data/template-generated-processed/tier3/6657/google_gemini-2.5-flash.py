from fractions import Fraction

def solve():
    """Index: 6657.
    Returns: the number of dice the boys need to buy.
    """
    # L1
    mark_percentage_12_sided = Fraction(60, 100) # 60% of them are 12 sided
    mark_total_dice = 10 # Mark has a bag of 10 dice
    mark_12_sided_dice = mark_percentage_12_sided * mark_total_dice

    # L2
    james_percentage_12_sided = Fraction(75, 100) # 75% of them are 12 sided
    james_total_dice = 8 # James has a bag of 8 dice
    james_12_sided_dice = james_percentage_12_sided * james_total_dice

    # L3
    total_dice_needed = 14 # total of 14 dice
    dice_to_buy = total_dice_needed - mark_12_sided_dice - james_12_sided_dice

    # FA
    answer = dice_to_buy
    return answer