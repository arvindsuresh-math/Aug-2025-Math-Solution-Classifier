def solve():
    """Index: 6556.
    Returns: the number of popsicle sticks Danielle will be left with.
    """
    # L1
    initial_money = 10 # She has $10 for supplies
    mold_cost = 3 # buys one set of molds for $3
    stick_pack_cost = 1 # a pack of 100 popsicle sticks for $1
    money_left_after_initial_supplies = initial_money - mold_cost - stick_pack_cost

    # L2
    juice_bottle_cost = 2 # costs $2
    num_juice_bottles = money_left_after_initial_supplies / juice_bottle_cost

    # L3
    popsicles_per_bottle = 20 # makes 20 popsicles
    total_popsicles_made = popsicles_per_bottle * num_juice_bottles

    # L4
    initial_sticks = 100 # a pack of 100 popsicle sticks
    sticks_left = initial_sticks - total_popsicles_made

    # FA
    answer = sticks_left
    return answer