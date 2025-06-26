def solve(
    pinata_cost: int = 13,  # unicorn piñata cost
    reeses_bags: int = 4,  # number of Reese's bags
    reeses_bag_cost: int = 9,  # cost per bag of Reese's
    snickers_bags: int = 3,  # number of Snickers bags
    snickers_bag_cost: int = 5,  # cost per bag of Snickers
    skittles_bags: int = 5,  # number of Skittles bags
    skittles_bag_cost: int = 7  # cost per bag of Skittles
):
    """Index: 45.
    Returns: the total cost of the unicorn piñata and all treats."""

    #: L1
    reeses_total_cost = reeses_bags * reeses_bag_cost

    #: L2
    snickers_total_cost = snickers_bags * snickers_bag_cost

    #: L3
    skittles_total_cost = skittles_bags * skittles_bag_cost

    answer = pinata_cost + reeses_total_cost + snickers_total_cost + skittles_total_cost  # FINAL ANSWER
    return answer