def solve(
    milk_gallons: int = 16,  # "Bill milked his cow and got 16 gallons of milk."
    fraction_to_sour_cream: float = 1/4,  # "He turned 1/4 into sour cream"
    fraction_to_butter: float = 1/4,  # "1/4 into butter"
    milk_per_butter: int = 4,  # "It takes 4 gallons of milk to make one gallon of butter"
    milk_per_sour_cream: int = 2,  # "2 gallons of milk to make 1 gallon of sour cream"
    price_butter: int = 5,  # "butter for $5/gallon"
    price_sour_cream: int = 6,  # "sour cream for $6/gallon"
    price_milk: int = 3  # "whole milk for $3/gallon"
):
    """Index: 5464.
    Returns: the total amount of money Bill makes from selling his dairy products.
    """
    #: L1 - Calculate the gallons of milk used for sour cream.
    milk_for_sour_cream = milk_gallons * fraction_to_sour_cream

    #: L2 - Calculate the gallons of butter made from the milk allocated for butter.
    milk_for_butter = milk_gallons * fraction_to_butter

    #: L3 - Convert the milk allocated for butter into gallons of butter.
    butter_gallons = milk_for_butter / milk_per_butter

    #: L4 - Convert the milk allocated for sour cream into gallons of sour cream.
    sour_cream_gallons = milk_for_sour_cream / milk_per_sour_cream

    #: L5 - Compute the remaining milk that is kept as whole milk.
    whole_milk_gallons = milk_gallons - milk_for_sour_cream - milk_for_butter

    #: L6 - Calculate the total revenue from selling whole milk.
    revenue_milk = whole_milk_gallons * price_milk

    #: L7 - Calculate the total revenue from selling sour cream.
    revenue_sour_cream = sour_cream_gallons * price_sour_cream

    #: L8 - Calculate the total revenue from selling butter.
    revenue_butter = butter_gallons * price_butter

    #: L9 - Sum up all the revenues to get the total money made.
    total_revenue = revenue_milk + revenue_sour_cream + revenue_butter

    answer = total_revenue  # FINAL ANSWER
    return answer