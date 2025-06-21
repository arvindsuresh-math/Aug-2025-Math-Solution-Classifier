def solve(
    total_milk: int = 16, # Bill milked his cow and got 16 gallons of milk.
    fraction_sour_cream_butter: float = 1/4, # He turned 1/4 into sour cream, and 1/4 into butter
    milk_for_butter: int = 4, # It takes 4 gallons of milk to make one gallon of butter
    milk_for_sour_cream: int = 2, # and 2 gallons of milk to make 1 gallon of sour cream.
    price_butter: int = 5, # Bill sells butter for $5/gallon
    price_sour_cream: int = 6, # sour cream for $6/gallon
    price_whole_milk: int = 3 # and whole milk for $3/gallon
):
    """Index: 5464.
    Returns: the total amount of money Bill makes.
    """
    #: L1
    milk_for_sour_cream_and_butter = total_milk * fraction_sour_cream_butter

    #: L2
    gallons_butter = milk_for_sour_cream_and_butter / milk_for_butter

    #: L3
    gallons_sour_cream = milk_for_sour_cream_and_butter / milk_for_sour_cream

    #: L4
    gallons_whole_milk = total_milk - milk_for_sour_cream_and_butter - milk_for_sour_cream_and_butter

    #: L5
    money_from_milk = gallons_whole_milk * price_whole_milk

    #: L6
    money_from_sour_cream = gallons_sour_cream * price_sour_cream

    #: L7
    total_money = money_from_milk + money_from_sour_cream + (gallons_butter * price_butter)

    answer = total_money # FINAL ANSWER
    return answer