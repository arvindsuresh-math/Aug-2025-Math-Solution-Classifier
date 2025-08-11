def solve():
    """Index: 4569.
    Returns: the total cost of feed corn per year.
    """
    # L1
    num_sheep = 8 # 8 sheep
    sheep_acres_per_month = 1 # each sheep eats 1 acre of grass per month
    num_cattle = 5 # 5 cattle
    cattle_acres_per_month = 2 # each cow eats 2 acres of grass per month
    total_acres_grass = 144 # 144 acres of grass
    total_acres_eaten_per_month = (num_cattle * cattle_acres_per_month) + (num_sheep * sheep_acres_per_month)

    # L2
    months_grazing = total_acres_grass / total_acres_eaten_per_month

    # L3
    months_per_year = 12 # WK
    months_needing_feed = months_per_year - months_grazing

    # L4
    sheep_feed_months_per_bag = 2 # each sheep for 2 months
    bags_per_sheep = months_needing_feed / sheep_feed_months_per_bag
    total_bags_for_sheep = num_sheep * bags_per_sheep

    # L5
    cattle_feed_months_per_bag = 1 # each cow for 1 month
    bags_per_cattle = months_needing_feed / cattle_feed_months_per_bag
    total_bags_for_cattle = num_cattle * bags_per_cattle

    # L6
    total_bags_of_feed_corn = total_bags_for_sheep + total_bags_for_cattle

    # L7
    cost_per_bag = 10 # $10 per bag
    total_cost_feed_corn = total_bags_of_feed_corn * cost_per_bag

    # FA
    answer = total_cost_feed_corn
    return answer