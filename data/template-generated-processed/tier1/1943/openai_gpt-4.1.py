def solve():
    """Index: 1943.
    Returns: the total cost for the family to enter the park and visit one attraction.
    """
    # L1
    num_kids = 4 # 4 children
    num_parents = 2 # their parents
    num_grandmothers = 1 # her grandmother
    total_persons = num_kids + num_parents + num_grandmothers

    # L2
    entrance_ticket_price = 5 # entrance ticket to the park is $5
    entrance_total = total_persons * entrance_ticket_price

    # L3
    attraction_ticket_kid = 2 # ticket costs $2 for kids
    attraction_kids_total = num_kids * attraction_ticket_kid

    # L4
    num_adults = num_parents + num_grandmothers # parents and grandmother
    attraction_ticket_adult = 4 # ticket costs $4 for parents
    attraction_adults_total = num_adults * attraction_ticket_adult

    # L5
    total_cost = entrance_total + attraction_kids_total + attraction_adults_total

    # FA
    answer = total_cost
    return answer