def solve():
    """Index: 7010.
    Returns: the cost of the appetizer per person.
    """
    # L1
    num_chip_bags = 3 # 3 individual bags of potato chips
    cost_per_chip_bag = 1.00 # $1.00 each
    cost_chips = num_chip_bags * cost_per_chip_bag

    # L2
    cost_creme_fraiche = 5.00 # creme fraiche that costs $5.00
    cost_caviar = 73.00 # the $73.00 caviar
    total_appetizer_cost = cost_chips + cost_creme_fraiche + cost_caviar

    # L3
    num_people_served = 3 # serve 3 people
    cost_per_person = total_appetizer_cost / num_people_served

    # FA
    answer = cost_per_person
    return answer