def solve():
    """Index: 1590.
    Returns: the amount of money John saves per day compared to what he used to spend.
    """
    # L1
    old_num_coffees = 4 # John used to buy 4 coffees a day
    cut_fraction = 2 # he cut the number of coffees he drinks in half
    new_num_coffees = old_num_coffees / cut_fraction

    # L2
    old_price = 2 # $2 each
    price_increase_fraction = 0.5 # raised the price by 50%
    price_increase = old_price * price_increase_fraction

    # L3
    new_price = old_price + price_increase

    # L4
    new_total = new_price * new_num_coffees

    # L5
    old_total = old_num_coffees * old_price

    # L6
    answer = old_total - new_total
    return answer