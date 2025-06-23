def solve(
    initial_milk_gallons: int = 16, # Bill milked his cow and got 16 gallons of milk
    fraction_to_sour_cream: float = 1/4, # He turned 1/4 into sour cream
    fraction_to_butter: float = 1/4, # 1/4 into butter
    milk_per_gallon_butter: int = 4, # It takes 4 gallons of milk to make one gallon of butter
    milk_per_gallon_sour_cream: int = 2, # and 2 gallons of milk to make 1 gallon of sour cream
    price_per_gallon_butter: int = 5, # Bill sells butter for $5/gallon
    price_per_gallon_sour_cream: int = 6, # sour cream for $6/gallon
    price_per_gallon_whole_milk: int = 3 # and whole milk for $3/gallon
):
    """Index: 5464.
    Returns: the total amount of money Bill makes from selling the products.
    """
    #: L1
    milk_for_sour_cream = initial_milk_gallons * fraction_to_sour_cream
    milk_for_butter = initial_milk_gallons * fraction_to_butter # Although L1 only shows one calculation, the problem implies 1/4 for each

    #: L2
    gallons_butter = milk_for_butter / milk_per_gallon_butter

    #: L3
    gallons_sour_cream = milk_for_sour_cream / milk_per_gallon_sour_cream

    #: L4
    gallons_whole_milk = initial_milk_gallons - milk_for_sour_cream - milk_for_butter

    #: L5
    money_from_whole_milk = gallons_whole_milk * price_per_gallon_whole_milk

    #: L6
    money_from_sour_cream = gallons_sour_cream * price_per_gallon_sour_cream

    # Calculate money from butter (implied step before L7)
    money_from_butter = gallons_butter * price_per_gallon_butter

    #: L7
    total_money = money_from_whole_milk + money_from_sour_cream + money_from_butter

    answer = total_money # FINAL ANSWER
    return answer