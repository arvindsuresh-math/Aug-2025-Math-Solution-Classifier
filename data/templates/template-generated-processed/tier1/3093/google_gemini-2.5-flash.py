def solve():
    """Index: 3093.
    Returns: the total cost Madeline will spend on seeds.
    """
    # L1
    flowers_needed = 20 # plant 20 flowers
    death_rate_multiplier = 2 # about half of the seeds she plants will die
    seeds_to_plant = death_rate_multiplier * flowers_needed

    # L2
    seeds_per_pack = 25 # 25 seeds per pack
    packs_needed = (seeds_to_plant + seeds_per_pack - 1) // seeds_per_pack

    # L3
    cost_per_pack = 5 # Each pack is $5
    total_cost = packs_needed * cost_per_pack

    # FA
    answer = total_cost
    return answer