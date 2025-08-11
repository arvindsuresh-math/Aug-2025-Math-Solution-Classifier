def solve():
    """Index: 2317.
    Returns: the final bill total including tip.
    """
    # L1
    num_twins = 2 # twin boys both ordered a cheeseburger
    cheeseburger_price = 13.50 # cheeseburger and fries for $13.50 each
    twins_cheeseburgers_total = num_twins * cheeseburger_price

    # L2
    num_people = 4 # party for 4 people
    dessert_price = 6.00 # dessert that cost $6.00 each
    dessert_total = num_people * dessert_price

    # L3
    mom_lobster_price = 25.50 # lobster for $25.50
    dad_steak_price = 35.00 # steak for $35.00
    appetizer_price = 8.50 # appetizer that cost 8.50
    meals_total = mom_lobster_price + dad_steak_price + twins_cheeseburgers_total + appetizer_price + dessert_total

    # L4
    tip_percent_num = 20 # 20% tip
    tip_percent_decimal = 0.20 # .20*120.00
    percent_factor = 0.01 # WK
    tip_amount = tip_percent_num * percent_factor * meals_total

    # L5
    final_total = meals_total + tip_amount

    # FA
    answer = final_total
    return answer