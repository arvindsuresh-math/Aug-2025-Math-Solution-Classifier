def solve(
    total_milk: int = 16,  # Bill milked his cow and got 16 gallons of milk
    fraction_sour_cream: float = 1/4,  # He turned 1/4 into sour cream
    fraction_butter: float = 1/4,  # 1/4 into butter
    milk_per_butter: int = 4,  # It takes 4 gallons of milk to make one gallon of butter
    milk_per_sour_cream: int = 2,  # 2 gallons of milk to make 1 gallon of sour cream
    price_butter: int = 5,  # Butter sells for $5/gallon
    price_sour_cream: int = 6,  # Sour cream sells for $6/gallon
    price_milk: int = 3  # Whole milk sells for $3/gallon
):
    """Index: 5464.
    Returns: the total money Bill makes from selling butter, sour cream, and whole milk.
    """
    #: L1
    milk_sour_cream = total_milk * fraction_sour_cream
    milk_butter = total_milk * fraction_butter

    #: L2
    gallons_butter = milk_butter / milk_per_butter

    #: L3
    gallons_sour_cream = milk_sour_cream / milk_per_sour_cream

    #: L4
    gallons_whole_milk = total_milk - milk_butter - milk_sour_cream

    #: L5
    money_milk = gallons_whole_milk * price_milk

    #: L6
    money_sour_cream = gallons_sour_cream * price_sour_cream

    #: L7
    money_butter = gallons_butter * price_butter

    total_money = money_milk + money_sour_cream + money_butter

    answer = total_money  # FINAL ANSWER
    return answer