def solve():
    """Index: 160.
    Returns: the total amount John spent altogether.
    """
    # L1
    other_people = 3 # splits the cost with 3 other people
    john = 1 # John himself
    total_people = other_people + john

    # L2
    burger_pounds = 100 # 100 pounds of burgers
    burger_price_per_pound = 3 # $3 per pound
    burger_total = burger_pounds * burger_price_per_pound

    # L3
    condiments_and_propane = 80 # $80 of condiments and propane
    total_cost = burger_total + condiments_and_propane

    # L4
    each_paid = total_cost / total_people

    # L5
    alcohol_cost = 200 # alcohol costs $200
    john_total = alcohol_cost + each_paid

    # FA
    answer = john_total
    return answer