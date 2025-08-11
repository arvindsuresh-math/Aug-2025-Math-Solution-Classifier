def solve():
    """Index: 2908.
    Returns: the total amount of money Andrew donates to the homeless shelter.
    """
    # L1
    total_earnings = 400 # The bake sale earns a total of $400
    ingredient_cost = 100 # Andrew keeps $100 to cover the cost of ingredients
    remaining_money_after_costs = total_earnings - ingredient_cost

    # L2
    donation_divisor = 2 # half of the remaining total
    shelter_donation_from_sale = remaining_money_after_costs / donation_divisor

    # L3
    personal_donation = 10 # donate $10 from his own piggy bank
    total_shelter_donation = shelter_donation_from_sale + personal_donation

    # FA
    answer = total_shelter_donation
    return answer