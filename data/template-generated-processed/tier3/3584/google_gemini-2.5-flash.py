def solve():
    """Index: 3584.
    Returns: the number of months it would take Mary to save the target amount.
    """
    # L1
    washing_cars_earnings = 20 # $20 washing cars
    walking_dogs_earnings = 40 # $40 walking dogs
    monthly_earnings = washing_cars_earnings + walking_dogs_earnings

    # L2
    savings_divisor = 2 # half of that money
    monthly_savings = monthly_earnings / savings_divisor

    # L3
    target_savings = 150 # save $150
    months_to_save = target_savings / monthly_savings

    # FA
    answer = months_to_save
    return answer