def solve():
    """Index: 4638.
    Returns: how much more Sonja will spend than the rest of the office put together.
    """
    # L1
    bread_cost = 3 # $3 a loaf
    cold_cuts_cost = 23 # $23
    sonja_total_spend = bread_cost + cold_cuts_cost

    # L2
    num_people = 5 # Five people are planning a party
    soda_cost_per_person = 1 # $1 per person
    num_cracker_boxes = 2 # two boxes of crackers
    cracker_cost_per_box = 2 # $2 per box
    soda_total_cost = num_people * soda_cost_per_person
    barbara_total_spend = soda_total_cost + (num_cracker_boxes * cracker_cost_per_box)

    # L3
    num_cheese_doodle_packages = 2 # two packages of Cheese Doodles
    cheese_doodle_cost_per_package = 3 # $3 per package
    mario_rick_total_spend = num_cheese_doodle_packages * cheese_doodle_cost_per_package

    # L4
    danica_spend = 4 # $4
    rest_of_office_spend = barbara_total_spend + mario_rick_total_spend + danica_spend

    # L5
    sonja_more_than_rest = sonja_total_spend - rest_of_office_spend

    # FA
    answer = sonja_more_than_rest
    return answer