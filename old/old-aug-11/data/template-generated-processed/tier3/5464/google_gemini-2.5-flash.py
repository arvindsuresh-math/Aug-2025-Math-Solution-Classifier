from fractions import Fraction

def solve():
    """Index: 5464.
    Returns: the total amount of money Bill makes.
    """
    # L1
    total_milk_gallons = 16 # 16 gallons of milk
    fraction_turned = Fraction(1, 4) # 1/4 into sour cream, 1/4 into butter
    milk_for_product = total_milk_gallons * fraction_turned

    # L2
    milk_per_gallon_butter = 4 # 4 gallons of milk to make one gallon of butter
    gallons_per_gallon_butter_unit = 1 # WK
    gallons_of_butter = milk_for_product / milk_per_gallon_butter / gallons_per_gallon_butter_unit

    # L3
    milk_per_gallon_sour_cream = 2 # 2 gallons of milk to make 1 gallon of sour cream
    gallons_per_gallon_sour_cream_unit = 1 # WK
    gallons_of_sour_cream = milk_for_product / milk_per_gallon_sour_cream / gallons_per_gallon_sour_cream_unit

    # L4
    remaining_whole_milk = total_milk_gallons - milk_for_product - milk_for_product

    # L5
    price_whole_milk_per_gallon = 3 # whole milk for $3/gallon
    cost_whole_milk = remaining_whole_milk * price_whole_milk_per_gallon

    # L6
    price_sour_cream_per_gallon = 6 # sour cream for $6/gallon
    cost_sour_cream = gallons_of_sour_cream * price_sour_cream_per_gallon

    # Implicit calculation for butter cost, not a numbered line in solution
    price_butter_per_gallon = 5 # butter for $5/gallon
    cost_butter = gallons_of_butter * price_butter_per_gallon

    # L7
    total_money_earned = cost_whole_milk + cost_sour_cream + cost_butter

    # FA
    answer = total_money_earned
    return answer